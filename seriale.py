import serial
import time
import binascii

ser = serial.Serial("/dev/tty.SLAB_USBtoUART")
#ser.open()
ser.isOpen()
input=1
while 1:
    input = raw_input(">> ")
    if (input == "exit"):
        ser.close()
        exit()
    else:
        ser.write(input + '\r\n')
        out = ''
        time.sleep(1)
        while (ser.inWaiting() > 0):
            out = ser.read(1)
            print ord(out)
            #out += ser.read(255)
        if out != '':
            print ">> " + out
