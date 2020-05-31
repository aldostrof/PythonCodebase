#!/usr/bin/env python3

import socket
import sys

print("UDP Server\n")

HOST = "127.0.0.1"
PORT = int(input("Enter local listening port: "))

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print("Listening..\n")
    while True:
    	data, address = s.recvfrom(32)
    	if not data:
    		break
    	print('Connected by', address)
    	print("Received:", repr(data))
