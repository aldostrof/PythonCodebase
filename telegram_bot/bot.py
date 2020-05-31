#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

Simple example showing how to create a basic telegram bot.
Bot should be registered by contacting @BotFather, with the following messages:
    - /start                : starts the BotFather
    - /newbot               : register new bot
    - <insert bot name>
    - <insert bot username>
Bot is then created, and can be reached at url: t.me/<bot_username>.
Next, you should take note of the bot token as it is required to interact with it
through python.
Other useful commands to use with @BotFather:
    - /setcommands          : can be used to add new commands to the bot; follow the indications.
    - /setuserpic           : can be used to modify bot's profile picture.
    - /setdescription       : can be used to modify bot's description text.
    - /setabout             : can be used to modify bot's about section.
For other commands, visit: https://core.telegram.org/bots/api

Please note that the python script must run continuously in order for the bot
to be active and reachable.

"""

import telepot
from telepot.loop import MessageLoop
import pprint
import configparser
import time

TOKEN = ''

def init_token():
    global TOKEN
    config = configparser.ConfigParser()
    config.read('bot_token.config')
    TOKEN = config['TOKEN']['BotToken']
    print("[BOT][DEBUG] Read token: {}".format(TOKEN))

def on_chat_message(msg):
    resp = bot.getUpdates()
    print("[BOT][DEBUG] Received:\n")
    pprint.pprint(resp)

    name = resp[0].get("message").get("from").get("first_name")
    surname = resp[0].get("message").get("from").get("last_name")
    chat_id = resp[0].get("message").get("from").get("id")
    msg = ''
    
    if 'text' in resp[0].get("message"):
        msg = resp[0].get("message").get("text")

    bot.sendMessage(chat_id, "Hi there, {} {}.\nYour chat ID is {}.\n".format(
        name,
        surname,
        chat_id
    ))

    if len(str(msg)) > 0:
       bot.sendMessage(chat_id, "You typed: {}".format(str(msg))) 

    # quick view at received message; use content_type to detect if the
    # msg is a text (this is not always the case).
    # content_type, chat_type, chat_id = telepot.glance(msg)


if __name__ == "__main__":
    init_token()
    bot = telepot.Bot(TOKEN)
    print("[BOT][DEBUG] Bot is active! You can now reach me on Telegram.")
    MessageLoop(bot, on_chat_message).run_as_thread()
    while 1:
        time.sleep(10)
