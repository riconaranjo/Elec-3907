import time

from neopixel import *

import argparse
import signal
import sys

# LED strip configuration:
LED_COUNT      = 80    # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 100     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour orderingfrom neopixel import*

maxLimitX = 50 # in cm
maxLimitY = 50 # in cm

# there are 54 LEDs, in two strips of 27 LEDs
MaxLedX = 26 # from 0 to 26
MaxLedY = 53 # from 27 to 53

white = Color(50,50,50)
off = Color(0,0,0)

def lights(x1, y1, x2, y2) :

    # 2 distinct points

    # point 1 valid [this is also repeated values with (x2,y2() = (0,0)]

    # point 2 valid

    # no valid points

    return

# this is used by neopixel library
def signal_handler(signal, frame):
    colorWipe(strip, Color(0,0,0))
    sys.exit(0)

# this is used by neopixel library
def opt_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', action='store_true', help='clear the display on exit')
    args = parser.parse_args()
    if args.c:
        signal.signal(signal.SIGINT, signal_handler)

# this contains all the LED indices used in setPixelColor(), for each actual LED
# led[x] will turn on xth LED, and the two adjacent LEDs.
led = [[0, 1, 2, 3], [0, 1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10, 11], [10, 11, 12], [11, 12, 13], [12, 13, 14, 15], [14, 15, 16], [15, 16, 17], [16, 17, 18, 19], [18, 19, 20], [19, 20, 21], [20, 21, 22, 23], [22, 23, 24], [23, 24, 25], [24, 25, 26, 27], [26, 27, 28], [27, 28, 29], [28, 29, 30, 31], [30, 31, 32], [31, 32, 33], [32, 33, 34, 35], [32, 33, 34, 35], [36, 37, 38, 39], [36, 37, 38, 39], [38, 39, 40], [39, 40, 41], [40, 41, 42, 43], [42, 43, 44], [43, 44, 45], [44, 45, 46, 47], [46, 47, 48], [47, 48, 49], [48, 49, 50, 51], [50, 51, 52], [51, 52, 53], [52, 53, 54, 55], [54, 55, 56], [55, 56, 57], [56, 57, 58, 59], [58, 59, 60], [59, 60, 61], [60, 61, 62, 63], [62, 63, 64], [63, 64, 65], [64, 65, 66, 67], [66, 67, 68], [67, 68, 69], [68, 69, 70, 71], [68, 69, 70, 71]]

def convertIndexX(index) :
    if(index > MaxLedX) :
        print("invalid index for X LEDs")
        return -1
    return led[index]

def convertIndexY(index) :
    if(index > MaxLedY) :
        print("invalid index for Y LEDs")
        return -1
    i = index%(MaxLedX+1)
    return led[i]
    
def ledOnX(x):
    index = convertIndexX(x)
    strip.setPixelColor(index, white)
		
def ledOffY(x):
    index = convertIndexX(x)
    strip.setPixelColor(index, 0)
        
def ledOnY(y):
    index = convertIndexY(y)
    strip.setPixelColor(index, white)
		
def ledOffY(y):
    index = convertIndexY(y)
    strip.setPixelColor(index, 0)
     
def ledLightShow(x,y):
    # turn on first led at initial positon
    index_x = convertIndexX(x)
    index_y = convertIndexY(y)
    strip.setPixelColor(index_x, white)
    strip.setPixelColor(index_y, white)
    strip.show()
    #time.sleep(wait_ms/1000.0)
    
    xpos = index_x + 1
    xneg = index_x - 1
    ypos = index_y + 1
    yneg = index_y - 1
    
    # TODO: this
    while xpos <= MaxLedX and xneg > 0 and ypos <= max_y_led and yneg > 0: 
        strip.setPixelColor(x_array[xpos], white)

	strip.show()
	strip.setPixelColor(y_array[ypos], white)
	strip.show()
	strip.setPixelColor(x_array[xneg], white)
	strip.show()
	strip.setPixelColor(y_array[yneg], white)
	strip.show()
	
	xpos += 1
        xneg -= 1
        ypos += 1
        yneg -= 1
        time.sleep(0.1)

# Turn on one LED at time across strip
def ledWipe(strip, color, wait_ms=50):
	print(len(r))
	for i in range(len(r)) :
		# turn on each LED index
		strip.setPixelColor(r[i][0], color)
		strip.setPixelColor(r[i][1], color)
		strip.setPixelColor(r[i][2], color)
		
		if(len(r[i]) > 3) :	strip.setPixelColor(r[i][3], color)
		strip.show()

		# small pause with each LED on
		time.sleep(wait_ms/1000.0)

		# turn off this LED index before next one
		strip.setPixelColor(r[i][0], off)
		strip.setPixelColor(r[i][1], off)
		strip.setPixelColor(r[i][2], off)
		
		if(len(r[i]) > 3) : strip.setPixelColor(r[i][3], off)
		strip.show()

# Turn on one LED at time across strip
def ledsOff(strip, color, wait_ms=0):
	print(len(r))
	for i in range(len(r)) :
        # turn off each LED
		strip.setPixelColor(r[i][0], off)
		strip.setPixelColor(r[i][1], off)
		strip.setPixelColor(r[i][2], off)

        # small pause with each LED on, by default no pause
		time.sleep(wait_ms/1000.0)
		
		if(len(r[i]) > 3) : strip.setPixelColor(r[i][3], off)
		strip.show()

		
def leds(x,y):
    XledOn(x)
    YledOn(y)
    time.sleep(0.2)
    XledOff(x)
    YledOff(y)
    #ledLightShowx(x)
    #ledLightShowy(y)
    #ledsOff()
    
if __name__ == '__main__':
    # Process arguments
    opt_parse()

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    # Intialize the library (must be called once before other functions).
    strip.begin()   
ledsOff()
#f=open('test_numbers.txt')
#for line in f:
    
   
  #x,y = line.split(" ")
  #print("x,y = {},{}".format(x,y))
x=5
y=5
#leds(x/2,30 b+y/2)
  
#ledsOff()
  
