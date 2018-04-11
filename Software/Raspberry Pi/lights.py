import time

from neopixel import *

import argparse
import signal
import sys

# LED strip configuration:
LED_COUNT       = 80     # Number of LED pixels.
LED_PIN         = 18     # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10     # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ     = 800000 # LED signal frequency in hertz (usually 800 kHz)
LED_DMA         = 10     # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS  = 100    # Set to 0 for darkest and 255 for brightest
LED_INVERT      = False  # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL     = 0      # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP       = ws.WS2811_STRIP_GRB   # Strip type and colour orderingfrom neopixel import*

maxLimit = 45 # in cm

# there are 54 LEDs, in two strips of 27 LEDs
maxLimitLed= 26 # y from 0 to 26, y: from 27 to 53
conversion = 26/44

white = Color(10,10,10)
off = Color(0,0,0)

# this contains all the LED indices used in setPixelColor(), for each actual LED
# led[x] will turn on xth LED, and the two adjacent LEDs.
leds = [[0, 1, 2, 3], [0, 1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10, 11], [10, 11, 12], [11, 12, 13], [12, 13, 14, 15], [14, 15, 16], [15, 16, 17], [16, 17, 18, 19], [18, 19, 20], [19, 20, 21], [20, 21, 22, 23], [22, 23, 24], [23, 24, 25], [24, 25, 26, 27], [26, 27, 28], [27, 28, 29], [28, 29, 30, 31], [30, 31, 32], [31, 32, 33], [32, 33, 34, 35], [32, 33, 34, 35], [36, 37, 38, 39], [36, 37, 38, 39], [38, 39, 40], [39, 40, 41], [40, 41, 42, 43], [42, 43, 44], [43, 44, 45], [44, 45, 46, 47], [46, 47, 48], [47, 48, 49], [48, 49, 50, 51], [50, 51, 52], [51, 52, 53], [52, 53, 54, 55], [54, 55, 56], [55, 56, 57], [56, 57, 58, 59], [58, 59, 60], [59, 60, 61], [60, 61, 62, 63], [62, 63, 64], [63, 64, 65], [64, 65, 66, 67], [66, 67, 68], [67, 68, 69], [68, 69, 70, 71], [68, 69, 70, 71]]

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
strip.begin()
    
def lights(x1, y1, x2, y2) :
    opt_parse()
    
    # turn off all LEDs
    ledsOff()

    # 2 distinct points
    if(x1 != -1 and y1 != -1 and x2 != -1 and y2 != -1) :
        ledOnX(strip, x1)
        ledOnY(strip, y1)
        ledOnX(strip, x2)
        ledOnY(strip, y2)

    # point 1 valid [this is also repeated values with (x2,y2) = (0,0)]
    elif(x2 == -1 and y2 == -1 and not(x1 == -1 and y1 == -1)) :
        ledOnX(strip, x1)
        ledOnY(strip, y1)

    # point 2 valid
    elif(x1 == -1 and y1 == -1) :
        ledOnX(strip, x1)
        ledOnY(strip, y1)

    else :
        #lightshow()
        variable = 1

    strip.show()

# this is used by neopixel library
def signal_handler(signal, frame):
    ledsOff() 
    sys.exit(0)

# this is used by neopixel library
def opt_parse() :
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', action='store_true', help='clear the display on exit')
    args = parser.parse_args()
    if args.c:
        signal.signal(signal.SIGINT, signal_handler)

def convertIndexX(value) :
    index = value*26/44
    if(index > maxLimitLed) :
        print("invalid index for X LEDs, (value, index) = ", value, index)
        return -1
    #print("index x (value, index) = ", value, index)
    return leds[index]

def convertIndexY(value) :
    index = value*26/44
    if(index > maxLimitLed) :
        print("invalid index for Y LEDs, (value, index) = ", value, index)
        return -1
    #print("index y (value, index) = ", value, index)
    return leds[index+maxLimitLed+1]
    
def ledOnX(strip, x) :
    index = convertIndexX(x)
    toggleLeds(strip, index, white)
		
def ledOffX(strip, x):
    index = convertIndexX(x)
    toggleLeds(strip, index, off)
        
def ledOnY(strip, y):
    index = convertIndexY(y)
    toggleLeds(strip, index, white)
		
def ledOffY(strip, y):
    index = convertIndexY(y)
    toggleLeds(strip, index, off)
    
def toggleLeds(strip, index, colour) :
    strip.setPixelColor(index[0], white)
    strip.setPixelColor(index[1], white)
    strip.setPixelColor(index[2], white)
        
    if(len(index) > 3) :
        strip.setPixelColor(index[3], colour)

    #strip.show()

# Turn on one LED at time across strip
def ledWipe(strip, color, wait_ms=50):
    for i in range(len(leds)) :
        # turn on each LED index
        strip.setPixelColor(leds[i][0], color)
        strip.setPixelColor(leds[i][1], color)
        strip.setPixelColor(leds[i][2], color)
        
        if(len(leds[i]) > 3) :	strip.setPixelColor(leds[i][3], color)
        strip.show()

        # small pause with each LED on
        time.sleep(wait_ms/1000.0)

        # turn off this LED index before next one
        strip.setPixelColor(leds[i][0], off)
        strip.setPixelColor(leds[i][1], off)
        strip.setPixelColor(leds[i][2], off)
        
        if(len(leds[i]) > 3) : strip.setPixelColor(leds[i][3], off)
        strip.show()

# Turn on one LED at time across strip
def ledsOff() :
    
    for i in range(72) :
        # turn off each LED
        strip.setPixelColor(i, off)
        
    strip.show()
     
def ledLightShow(x1,y1,x2,y2):
    # turn on first led at initial positon
    index_x = convertIndexX(x1)
    index_y = convertIndexY(y1)
    toggleLeds(strip, index_x, white)
    toggleLeds(strip, index_y, white)
    index_x2 = convertIndexX(x2)
    index_y2 = convertIndexY(y2)
    toggleLeds(strip, index_x2, white)
    toggleLeds(strip, index_y2, white)
    strip.show()
    #time.sleep(wait_ms/1000.0)
    
    xpos = x1 + 1
    xneg = x1 - 1
    ypos = y1 + 1
    yneg = y1 - 1
    xpos2 = x2 + 1
    xneg2 = x2 - 1
    ypos2 = y2 + 1
    yneg2 = y2 - 1
    
    xpos3 = xpos
    xneg3 = xneg
    ypos3 = ypos
    yneg3 = yneg
    xpos4 = xpos2
    xneg4 = xneg2
    ypos4 = ypos2
    yneg4 = yneg2
    
    while xpos < maxLimit or xpos2 < maxLimit or xneg > 0 \
    or xneg2 > 0 or ypos < maxLimit or ypos2 < maxLimit \
    or yneg > 0 or yneg2 > 0 : 
        index_xpos = convertIndexX(xpos)
        index_ypos = convertIndexY(ypos)
        index_xneg = convertIndexX(xneg)
        index_yneg = convertIndexY(yneg)
        index_xpos2 = convertIndexX(xpos2)
        index_ypos2 = convertIndexY(ypos2)
        index_xneg2 = convertIndexX(xneg2)
        index_yneg2 = convertIndexY(yneg2)
        
        toggleLeds(strip,index_xpos, white)
        toggleLeds(strip,index_xneg, white)
        toggleLeds(strip,index_ypos, white)
        toggleLeds(strip,index_yneg, white)
        toggleLeds(strip,index_xpos2, white)
        toggleLeds(strip,index_xneg2, white)
        toggleLeds(strip,index_ypos2, white)
        toggleLeds(strip,index_yneg2, white)
	strip.show()
	if(xpos < maxLimit) : xpos += 1
        if(xneg > 0) : xneg -= 1
        if(ypos < maxLimit) : ypos += 1
        if(yneg > 0) : yneg -= 1
        if(xpos2 < maxLimit) : xpos2 += 1
        if(xneg2 > 0) : xneg2 -= 1
        if(ypos2 < maxLimit) : ypos2 += 1
        if(yneg2 > 0) : yneg2 -= 1
        time.sleep(0.1)
        #print(xpos,xpos2,xneg,xneg2,ypos,ypos2,yneg,yneg2)
        
    while xpos3 < maxLimit or xpos4 < maxLimit or xpos3 > 0 \
    or xpos4 > 0 or ypos3 < maxLimit or ypos4 < maxLimit \
    or yneg3 > 0 or yneg4 > 0 : 
        index_xpos3 = convertIndexX(xpos3)
        index_ypos3 = convertIndexY(ypos3)
        index_xpos3 = convertIndexX(xpos3)
        index_yneg3 = convertIndexY(yneg3)
        index_xpos4 = convertIndexX(xpos4)
        index_ypos4 = convertIndexY(ypos4)
        index_xpos4 = convertIndexX(xpos4)
        index_yneg4 = convertIndexY(yneg4)
        
        toggleLeds(strip,index_xpos3, off)
        toggleLeds(strip,index_xpos3, off)
        toggleLeds(strip,index_ypos3, off)
        toggleLeds(strip,index_yneg3, off)
        toggleLeds(strip,index_xpos4, off)
        toggleLeds(strip,index_xpos4, off)
        toggleLeds(strip,index_ypos4, off)
        toggleLeds(strip,index_yneg4, off)
	strip.show()
	if(xpos3 < maxLimit) : xpos3 += 1
        if(xpos3 > 0) : xpos3 -= 1
        if(ypos3 < maxLimit) : ypos3 += 1
        if(yneg3 > 0) : yneg3 -= 1
        if(xpos4 < maxLimit) : xpos4 += 1
        if(xpos4 > 0) : xpos4 -= 1
        if(ypos4 < maxLimit) : ypos4 += 1
        if(yneg4 > 0) : yneg4 -= 1
        time.sleep(0.1)
        #print(xpos,xpos4,xneg,xpos4,ypos,ypos2,yneg,yneg2)
        

def test(x1,y1,x2,y2):
    lights(x1,y1,x2,y2)
    ledLightShow(x1,y1,x2,y2)

if __name__ == '__main__':
    # Process arguments
    opt_parse()
    try :
        ledLightShow(10,10,30,30)
        ledsOff()
    except KeyboardInterrupt:
        ledsOff()
    # Create NeoPixel object with appropriate configuration.
##    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
##    strip.begin()
##    x=15
##    y=15
##    ledWipe(strip, off,0)
##    test(x,y,10,10)
    #ledsOff()
  
