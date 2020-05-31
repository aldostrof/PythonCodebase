#!/usr/bin/env python
from __future__ import print_function

import binascii
import pygatt

YOUR_DEVICE_ADDRESS = "C0:26:DF:00:AB:0E"
# Many devices, e.g. Fitbit, use random addressing - this is required to
# connect.
ADDRESS_TYPE = pygatt.BLEAddressType.random

def handle_indications(handle, value):
	print("Received indication from handle:", hex(handle))
	print("Received indication data: %s" % binascii.hexlify(value))


def handle_notifications(handle, value):
	print("Received notification from handle:", hex(handle))
	print("Received notification data: %s" % binascii.hexlify(value))

handle = 0
adapter = pygatt.GATTToolBackend()
adapter.start()
device = adapter.connect(YOUR_DEVICE_ADDRESS, address_type=ADDRESS_TYPE)

print("Connected!")

for uuid in device.discover_characteristics().keys():
	print("UUID:", uuid)

handle = device.get_handle("00002a05-0000-1000-8000-00805f9b34fb")
print("Subscribing handle:", hex(handle))
device.subscribe("00002a05-0000-1000-8000-00805f9b34fb", callback=handle_indications, indication=True)

handle = device.get_handle("00002a18-0000-1000-8000-00805f9b34fb")
print("Subscribing handle:", hex(handle))
device.subscribe("00002a18-0000-1000-8000-00805f9b34fb", callback=handle_notifications)

handle = device.get_handle("00002a52-0000-1000-8000-00805f9b34fb")
print("Subscribing handle:", hex(handle))
device.subscribe("00002a52-0000-1000-8000-00805f9b34fb", callback=handle_indications, indication=True)

handle = device.get_handle("00002a19-0000-1000-8000-00805f9b34fb")
print("Subscribing handle:", hex(handle))
device.subscribe("00002a19-0000-1000-8000-00805f9b34fb", callback=handle_notifications)

handle = device.get_handle("00001524-1212-efde-1523-785feabcd123")
print("Subscribing handle:", hex(handle))
device.subscribe("00001524-1212-efde-1523-785feabcd123", callback=handle_indications, indication=True)

handle = device.get_handle("00002a52-0000-1000-8000-00805f9b34fb")
print("Writing handle:", hex(handle))

device.char_write("00002a52-0000-1000-8000-00805f9b34fb", bytearray([0x01, 0x01]), wait_for_response=True)

print("Sleep..\n")
while(1):
	pass


