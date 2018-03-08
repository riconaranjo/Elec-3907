import time

from neopixel import *

import argparse
import signal
import sys
def signal_handler(signal, frame):
    colorWipe(strip, Color(0,0,0))
    sys.exit(0)

def opt_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', action='store_true', help='clear the display on exit')
    args = parser.parse_args()
    if args.c:
        signal.signal(signal.SIGINT, signal_handler)

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

max_x_limit = 50
max_y_limit = 50
white = Color(255,255,255)

def XledOn(x):
    strip.setPixelColor(x, white)
		
def XledOff(x):
    strip.setPixelColor(x, 0)
        
def YledOn(y):
    strip.setPixelColor(y, white)
		
def YledOff(y):
    strip.setPixelColor(y, 0)
     
def ledLightShowx(x):
    strip.setPixelColor(x, white)
    for x in range(strip.numPixels()):
	strip.setPixelColor(x, white)
	strip.show()
	
	#time.sleep(wait_ms/1000.0)
    while x >0:
	strip.setPixelColor(x, white)
	strip.show()
        x=x-1
	
	#time.sleep(wait_ms/1000.0)
def ledLightShowy(y):
    strip.setPixelColor(y, white)
    for y in range(strip.numPixels()):
	strip.setPixelColor(y, white)
	strip.show()
	
	#time.sleep(wait_ms/1000.0)
    while y >0:
	strip.setPixelColor(y, white)
	strip.show()
        y=y-1
	
	#time.sleep(wait_ms/1000.0)

def ledsOff():
    print('a')
    i=1
    while i < range(strip.numPixels()):
        strip.setPixelColor(i, white)
	strip.show()
	i=i+1

		
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
#leds(x/2,30+y/2)
  
#ledsOff()
  