#!/usr/bin python3

# This is a small python example to demonstrate how a TCP Client
# can connect to a remote host to send some fixed bytes.
# The application tries to estabilish a connection with the given
# couple (Host, Port) and then, when successfull, sends an array
# of fixed bytes, then terminates.
# Pair this example-application with the tcp_server.py application to build
# a complete use-case.

import socket
import time

DIM_ARRAY = 32
BYTE_TO_SEND = 2
MAX_ATTEMPTS = 5
attempts = 0

print("[TCP Client] Starting.\n")

# get the IP as a string
HOST = str(input("[TCP Client] Enter Remote Host IP: "))

# get the port as int
PORT = int(input("[TCP Client] Enter Remote port: "))
connected = 0

while connected == 0:
    
    # exit the loop if max attempts limit is reached
    if(MAX_ATTEMPTS == attempts):
        print("[TCP Client] Maximum number of attempts ({}) reached, exiting.\n".format(MAX_ATTEMPTS))
        break

    print("[TCP Client] Trying to connect to {}:{}\n".format(HOST, PORT))
    time.sleep(1)
    
    # try to open a socket to the couple (host, port)
    try:
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            connected = 1
            arr = bytearray([BYTE_TO_SEND]*DIM_ARRAY)
            s.sendall(arr)
            time.sleep(2)
            print("[TCP Client] Communication completed.\n")
    
    except(Exception):
        
        # try again if connection is not available (and update attempts number)
        print("[TCP Client] Failed connection.\n")
        connected = 0
        attempts = attempts + 1

