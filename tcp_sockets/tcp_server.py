#!/usr/bin python3

# This is a small python example to demonstrate how a TCP Server
# can listen on localhost to a specified port for client requests.
# The application just sets up the server configuration (host, port)
# and then waits for incoming connections.
# Then, when a TCP client connects, it just wait for BYTES_TO_RECEIVE bytes
# and then prints them, thus returning to wait for incoming connection.
# Listening is stopped and application is terminated on force-exit (ctrl+c).
# Pair this example-application with the tcp_client.py application to build
# a complete use-case.


import socket

BYTES_TO_RECEIVE = 32
HOST = "127.0.0.1"
PORT = int(input("[TCP Server] Enter local listening port: "))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    # bind and listen on selected port
    s.bind((HOST, PORT))
    s.listen()

    print("[TCP Server] Started TCP Server on {}:{}\n".format(HOST, PORT))

    while True:

        try:
            # block until any connection is received
            conn, addr = s.accept()
            
            # whenever we receive a connection request, un-block
            with conn:
                print("[TCP Server] Got connection request by:", addr)
                
                # just receive BYTES_TO_RECEIVE bytes from the connected client
                data = conn.recv(BYTES_TO_RECEIVE)
                if not data:
                    print("[TCP Server] Some error occurred while reading data from", addr)
                else:
                    print("[TCP Server] Received {} bytes: {}".format(len(data), repr(data)))
                
                print("[TCP Server] Communication completed.")
        
        except(Exception, KeyboardInterrupt):
            print("[TCP Server] Exiting.\n")
            break
    
