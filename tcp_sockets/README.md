### Description

This is an example on how to setup and run a TCP socket (both client and server) in Python.

### Instructions

* First of all, you can open the **tcp_sockets.code-workspace** file contained in the directory in order to
put yourself in the right environment.

* To execute the **TCP Client** code, open an integrated terminal into the active workspace by going to
View>Command Palette> then type "Terminal: Create New Integrated Terminal (In Active Workspace)
and run the following command: 
```console
$ python tcp_client.py
```
The program will then ask you to enter the remote IP address and the remote port to connect.

After that, the program will continuosly try to connect to the specified (IP, port) pair and, when the 
connection is established, it will try to send an **array of 32 bytes** populated with value **0x02** 
before terminating.

Note that, after 5 unsuccessfull connection attempts, the program will terminate its execution.

Also note that, in order to have a correct execution of the program, **you should have setup a 
TCP server listening on the selected (IP, port) pair.**

* To execute the **TCP Server** code, open an integrated terminal into the active workspace by going to
View>Command Palette> then type "Terminal: Create New Integrated Terminal (In Active Workspace)
and run the following command: 
```console
$ python tcp_server.py
```
The program will then ask you to enter the local port to use when listening for new incoming connection
requests.

Please note that the server will always use the **localhost** address (127.0.0.1) along with the port you
select as input.

After that, the program blocks waiting for new requests and, when one arrives, it just receives 32 bytes
of data and then prints those bytes.

At the end, the program returns to wait for incoming connections.
Please note that the TCP Server application can be paired with the TCP Client application to build a
complete use-case: you just have to run the TCP Server first, and then start the TCP Client by giving
in input the TCP Server informations you configured before.
