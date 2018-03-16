# main function for raspberry pi
# use python 2
import serial

from convert import *
from lights import *

arduino = serial.Serial('/dev/ttyACM0', 9600)

print("press ctrl + c to quit")
while true
    # read data from Arduino
    input = arduino.readline()
    if(input == "")
        # time.sleep(0.2)
        continue
    
    # parse data
    a1, a2, a3, b1, b2, b3 = input.strip().split(" ")

    # convert data to cartesian coordinates

    x1, y1, x2, y2 = convert(a1, a2, a3, b1, b2, b3)

    # turn on corresponding LEDs

    lights(x1, y1, x2, y2)