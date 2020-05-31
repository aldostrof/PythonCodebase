#!/usr/bin/env python3

import socket
import sys
import time

DIM_ARRAY = 32

print("UDP Client\n");

HOST = input("Enter remote Host IP: ")
PORT = int(input("Enter remote port: "))
connected = 0

while connected == 0:
	time.sleep(2)
	print("Trying to connect..")
	try:
		clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		while True:
			connected = 1
			arr = bytearray([3]*DIM_ARRAY)
			clientSock.sendto(arr, (HOST, PORT))
			print("Sent 32 bytes (0x03).\n")
			time.sleep(10)
	except Exception:
		connected = 0