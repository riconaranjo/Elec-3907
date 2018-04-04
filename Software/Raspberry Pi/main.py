# main function for raspberry pi
# use python 2
import serial

from convert import *
from lights import *

arduino = serial.Serial('/dev/ttyACM0', 9600)
#f = open("test_data_six.txt", "r")

print("press ctrl + c to quit")
try :
    while True :
        print("------")
        # read data from Arduino
        input = arduino.readline()
        # input = f.readline()
        print(input)
        if(input == "") :
            time.sleep(0.1)
            continue
        
        # parse data
        try :
            a1, a2, a3, b1, b2, b3 = input.strip().split(" ")
        except :
            print("Parsing error with: ", input)
            continue
        # print(a1, a2, a3, b1, b2, b3)
        # convert data to cartesian coordinates
        try :
            x1, y1, x2, y2 = convert(int(a1), int(a2), int(a3), int(b1), int(b2), int(b3))
            if(x1 == -1 and y1 == -1 and x2 == -1 and y2 == -1) :
                continue
        except :
            print("Conversion error with: ", input)
            continue
            

        print("converted values", x1, y1, x2, y2)
    ##
    ##    # turn on corresponding LEDs
    ##
        lights(int(x1), int(y1), int(x2), int(y2))
except KeyboardInterrupt :
    print("quitting")
    ledsOff()
    #pass
    
