# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
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
LED_DMA        = 5      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 100     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering

r = [[0, 1, 2, 3], [0, 1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10, 11], [10, 11, 12], [11, 12, 13], [12, 13, 14, 15], [14, 15, 16], [15, 16, 17], [16, 17, 18, 19], [18, 19, 20], [19, 20, 21], [20, 21, 22, 23], [22, 23, 24], [23, 24, 25], [24, 25, 26, 27], [26, 27, 28], [27, 28, 29], [28, 29, 30, 31], [30, 31, 32], [31, 32, 33], [32, 33, 34, 35], [32, 33, 34, 35], [36, 37, 38, 39], [36, 37, 38, 39], [38, 39, 40], [39, 40, 41], [40, 41, 42, 43], [42, 43, 44], [43, 44, 45], [44, 45, 46, 47], [46, 47, 48], [47, 48, 49], [48, 49, 50, 51], [50, 51, 52], [51, 52, 53], [52, 53, 54, 55], [54, 55, 56], [55, 56, 57], [56, 57, 58, 59], [58, 59, 60], [59, 60, 61], [60, 61, 62, 63], [62, 63, 64], [63, 64, 65], [64, 65, 66, 67], [66, 67, 68], [67, 68, 69], [68, 69, 70, 71], [68, 69, 70, 71]]#, [71, 72, 73], [72, 73, 74, 75], [74, 75, 76], [75, 76, 77], [76, 77, 78, 79], [76, 77, 78, 79]]
off = Color(0,0,0)
# Define functions which animate LEDs in various ways.
def ledWipe(strip, color, wait_ms=50):
	"""Wipe color across display a pixel at a time."""
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
		
def colorWipe2(strip, color, wait_ms=0):
	"""Wipe color across display a pixel at a time."""
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.setPixelColor(i-1, 0)
		strip.show()

		time.sleep(wait_ms/1000.0)
		
	strip.setPixelColor(strip.numPixels()-1, Color(0,0,0))

def theaterChase(strip, color, wait_ms=50, iterations=10):
	"""Movie theater light style chaser animation."""
	for j in range(iterations):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, color)
			strip.show()
			time.sleep(wait_ms/1000.0)
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, 0)

def wheel(pos):
	"""Genera)
			for i in range(0, strip.numPixelste rainbow colors across 0-255 positions."""
	if pos < 85:
		return Color(pos * 3, 255 - pos * 3, 0)
	elif pos < 170:
		pos -= 85
		return Color(255 - pos * 3, 0, pos * 3)
	else:
		pos -= 170
		return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
	"""Draw rainbow that fades across all pixels at once."""
	for j in range(256*iterations):
		for i in range(strip.numPixels()):
			setPixelColorstrip.setPixelColor(i, wheel((i+j) & 255))
		strip.show()
		time.sleep(wait_ms/1000.0)

def rainbowCycle(strip, wait_ms=20, iterations=5):
	"""Draw rainbow that uniformly distributes itstrip.setPixelColor(elf across all pixels."""
	for j in range(256*iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
		strip.show()
		time.sleep(wait_ms/1000.0)

def theaterChaseRainbow(strip, wait_ms=50):
	"""Rainbow movie theater light style chaser animation."""
	for j in range(256):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, wheel((i+j) % 255))
			strip.show()
			time.sleep(wait_ms/1000.0)
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, 0)

# Main program logic follows:
if __name__ == '__main__':
        # Process arguments
        opt_parse()

	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
	# Intialize the library (must be called once before other functions).
	strip.begin()

	print ('Press Ctrl-C to quit.')
	colorWipe2(strip, Color(0, 0, 0))
        colorWipe(strip, Color(50, 50, 50))
        color = Color(50, 50, 50)
        
        
##        strip.setPixelColor(0, color)
##        strip.setPixelColor(1, color)
##        strip.setPixelColor(2, color)
##	strip.show()
        #time.sleep(3)
        #strip.setPixelColor(0, color)
        #strip.setPixelColor(1, color)
        #strip.setPixelColor(2, color)
        #strip.setPixelColor(3, color)
        #strip.setPixelColor(4, color)
        #strip.setPixelColor(5, color)
        #strip.setPixelColor(6, color)
        #strip.setPixelColor(7, color)
        #strip.setPixelColor(8, color)
        #strip.setPixelColor(9, color)
        #strip.setPixelColor(10, color)
        #strip.setPixelColor(11, color)
        #strip.setPixelColor(12, color)
        #strip.setPixelColor(13, color)
        #strip.setPixelColor(14, color)
        #strip.setPixelColor(15, color)
        #strip.setPixelColor(6, color)
	#strip.show()
        #time.sleep(3)
##        strip.setPixelColor(0, color)
##        strip.setPixelColor(2, color)
##        strip.setPixelColor(3, color)
##	strip.show()
##        time.sleep(3)
        colorWipe2(strip, Color(0, 0, 0))

##        strip.setPixelColor(1, Color(0, 100, 0))
##        strip.setPixelColor(20, Color(0, 100, 0))
##        strip.setPixelColor(40, Color(0, 100, 0))
##        strip.setPixelColor(60, Color(0, 100, 0))
##        strip.setPixelColor(79, Color(0, 100, 0))
        #colorWipe2(strip, Color(100, 100, 100))

##        colorWipe(strip, 0x000000)
##        strip.setPixelColor(0, 0xffffff)
##	while True:
##		print ('Color wipe animations.')
##		colorWipe(strip, Color(255, 0, 0))  # Red wipe
##		colorWipe(strip, Color(0, 255, 0))  # Blue wipe
##		colorWipe(strip, Color(0, 0, 255))  # Green wipe
##		print ('Theater chase animations.')
##		theaterChase(strip, Color(127, 127, 127))  # White theater chase
##		theaterChase(strip, Color(127,   0,   0))  # Red theater chase
##		theaterChase(strip, Color(  0,   0, 127))  # Blue theater chase
##		print ('Rainbow animations.')
##		rainbow(strip)
##		rainbowCycle(strip)
##		theaterChaseRainbow(strip)
##		print ('turn off')
##		colorWipe(strip, Color(0, 0, 0))
