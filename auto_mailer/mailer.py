import pathlib
import smtplib
import configparser
import traceback
import urllib.request
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

_MAX_TRIES     = 5

class EmailAgent:

    _ROOT_DIR      = pathlib.Path(__file__).parent.absolute()
    _CONFIG_FILE   = _ROOT_DIR.joinpath("./email.config")
    _HTML_TEMPLATE = _ROOT_DIR.joinpath("./email/email.html")

    def __init__(self):
        self.init_config()

    def init_config(self):

        config     = None
        self._user = None
        self._psw  = None

        try:
            config = configparser.ConfigParser()
            config.read(self._CONFIG_FILE)
            self._user        = config['Credentials']['username']
            self._psw         = config['Credentials']['password']
            self._smtp_server = config['SMTP']['server']
            self._smtp_port   = config['SMTP']['port']
            self._subject = config['Email Config']['subject']
            self._content = config['Email Config']['text_content']
            self._image_url = config['Email Config']['image_url'] # may be empty
            self._contact_list = config['Email Config']['contact_list'].replace(" ", "").split(",")
        except Exception as e:
            raise ValueError("Cannot parse configuration values from file:{}".format(self._CONFIG_FILE))
        else:
            print("Initialized configuration values from file: {}".format(self._CONFIG_FILE))

    def build_msg(self):

        # Create message container - the correct MIME type is multipart/alternative.
        msg             = MIMEMultipart('alternative')
        txt_placeholder = "<!-- TXT_PLACEHOLDER -->"
        img_placeholder = "<!-- IMG_PLACEHOLDER -->"
        html            = None
        content_part1   = None
        content_part2   = None
        img_replaced    = None
        txt_replaced    = None

        if ((self._contact_list is None) or (not isinstance(self._contact_list, str)) and (not isinstance(self._contact_list, list))):
            raise TypeError("Receiver argument must be a single or a list of email addresses.")
        elif((self._subject is None) or (not isinstance(self._subject, str))):
            raise TypeError("Subject argument must be a valid string.")
        elif((self._content is None) or (not isinstance(self._content, str))):
            raise TypeError("Content argument must be a valid string.")
        elif(self._image_url is not None and len(self._image_url) != 0):
            # check that the url is reachable (return code == 200 OK)
            if(200 != urllib.request.urlopen(self._image_url).getcode()):
                raise ValueError("Invalid URL argument.")

        # Start building the message
        msg['From']    = self._user
        msg['Subject'] = self._subject

        # self._contact_list can be a list: if so, we must parse it as a string
        if isinstance(self._contact_list, list):
            msg['To'] = ", ".join(self._contact_list)
        else:
            msg['To'] = self._contact_list

        # read the html template into a string
        # all the replacements are made on the string, and not on the file
        try:
            with open(self._HTML_TEMPLATE, 'r') as f:
                html = f.read()
        except Exception as e:
            raise Exception("Could not read the HTML template file: {}".format(self._HTML_TEMPLATE))

        # Insert the image, if present
        if (self._image_url is not None and len(self._image_url) != 0):
            img_replaced = html.replace(img_placeholder, "<img src=\"{}\">".format(self._image_url), 1)
            if img_replaced == html:
                raise Exception("Cannot insert required image url: {} into html template.".format(self._image_url))
            else:
                html = img_replaced
                print("Inserted image url: {}".format(self._image_url, self._HTML_TEMPLATE))

        # Insert the text, if present
        txt_replaced = html.replace(txt_placeholder, self._content, 1)
        if txt_replaced == html:
            raise Exception("Cannot insert required text: {} into html template.".format(self._content))
        else:
            html = txt_replaced
            print("Inserted content text: {}".format(self._content, self._HTML_TEMPLATE))

        content_part1 = MIMEText(self._content, 'plain')
        content_part2 = MIMEText(html, 'html')

        # Attach parts into message container.
        # According to RFC 2046, the last part of a multipart message, in this case
        # the HTML message, is best and preferred.
        msg.attach(content_part1)
        msg.attach(content_part2)

        return msg

    def send_mail(self, msg):

        receivers = None
        session   = None

        # receiver may be a string (single receiver) or a list (multiple receivers)
        try:
            receivers = msg.get("To").split(", ")
        except Exception as e:
            raise ValueError("Cannot retrieve valid receivers for the mail to be sent.")
        else:
            if(len(receivers) == 0):
                raise ValueError("Cannot retrieve valid receivers for the mail to be sent.")

        try:
            # Connect to Gmail Server
            session = smtplib.SMTP(self._smtp_server, self._smtp_port)
            session.ehlo()
            session.starttls()
            session.ehlo()

            # Login to Gmail
            session.login(self._user, self._psw)

            # Send Email & Exit
            session.sendmail(self._user, receivers, msg.as_string())
            session.quit()
        except Exception as e:
            raise RuntimeError("Unable to send email.")
            traceback.print_exc()




if __name__ == "__main__":

    cnt    = 0
    # Constructor initializes params from config file
    sender = EmailAgent()
    msg    = sender.build_msg()

    # Try to send mail for MAX_TRIES times
    while(cnt < _MAX_TRIES):
        try:
            sender.send_mail(msg)
        except RuntimeError as e:
            print("Send mail - attempt {}/{} failed.".format(cnt, MAX_TRIES))
            cnt = cnt + 1
        else:
            break

    if cnt == _MAX_TRIES:
        raise RuntimeError("Reached maximum tries, aborting.")
    else:
        print("Done.")


