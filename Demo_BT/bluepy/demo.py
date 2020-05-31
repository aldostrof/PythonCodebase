from bluepy import btle
import binascii

 
ADDRESS = "C0:26:DF:00:AB:0E"

class MyDelegate(btle.DefaultDelegate):
    def __init__(self):
        btle.DefaultDelegate.__init__(self)

    def handleNotification(self, cHandle, data):
		print("Received event from handle:", hex(cHandle))
		print("Received data: %s" % binascii.hexlify(data))

print "Connecting..."
dev = btle.Peripheral(ADDRESS, btle.ADDR_TYPE_RANDOM)
dev.setDelegate( MyDelegate() )
 
print "Services..."
for svc in dev.services:
    print str(svc)
    print str(svc.uuid)


#0x2a05, indications
generic_attribute = dev.getServiceByUUID("00001801-0000-1000-8000-00805f9b34fb")
svc_changed = generic_attribute.getCharacteristics()[0]
svc_changed_vhandle = svc_changed.valHandle
print("SVC Changed with handle:", hex(svc_changed_vhandle))

dev.writeCharacteristic(svc_changed_vhandle+1, b"\x02\x00", withResponse=True)

#0x2a18, notification
glucose_svc = dev.getServiceByUUID("00001808-0000-1000-8000-00805f9b34fb")
glucose_measurement = glucose_svc.getCharacteristics()[0]
glucose_measurement_vhandle = glucose_measurement.valHandle
print("Glucose measurement with handle:", hex(glucose_measurement_vhandle))

dev.writeCharacteristic(glucose_measurement_vhandle+1, b"\x01\x00", withResponse=True)

#0x2a52, indication
glucose_racp = glucose_svc.getCharacteristics()[2]
glucose_racp_vhandle = glucose_racp.valHandle
print("RACP with handle:", hex(glucose_racp_vhandle))

dev.writeCharacteristic(glucose_racp_vhandle+1, b"\x02\x00", withResponse=True)

#0x2a19, notification
battery_svc = dev.getServiceByUUID("0000180f-0000-1000-8000-00805f9b34fb")
battery_lvl = battery_svc.getCharacteristics()[0]
battery_lvl_vhandle = battery_lvl.valHandle
print("Battery lvl with handle:", hex(battery_lvl_vhandle))

dev.writeCharacteristic(battery_lvl_vhandle+1, b"\x01\x00", withResponse=True)

#0x1524, indication
btn_svc = dev.getServiceByUUID("00001523-1212-efde-1523-785feabcd123")
btn = btn_svc.getCharacteristics()[0]
btn_svc_vhandle = btn.valHandle
print("BTN with handle:", hex(btn_svc_vhandle))

dev.writeCharacteristic(btn_svc_vhandle+1, b"\x02\x00", withResponse=True)

print("Setup completed\n")

# Get all reports..

dev.writeCharacteristic(glucose_racp_vhandle, b"\x01\x01", withResponse=True)


print("Going to sleep\n")

while True:
    if dev.waitForNotifications(5.0):
        # handleNotification() was called
        continue

    print("Waiting...")
    # Perhaps do something else here




