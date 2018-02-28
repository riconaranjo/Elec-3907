LED_COUNT = 60
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 5
LED_INVERT = False

import time
 
from neopixel import *

# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
	"""Wipe color across display a pixel at a time."""
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()
		time.sleep(wait_ms/1000.0)
		
# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT)
# Intialize the library (must be called once before other functions).
strip.begin()

print 'Press Ctrl-C to quit.'
while True:
	# Color wipe animations.
	colorWipe(strip, Color(255, 0, 0))  # Red wipe
	colorWipe(strip, Color(0, 255, 0))  # Blue wipe
	colorWipe(strip, Color(0, 0, 255))  # Green wipe
	# Theater chase animations.
	theaterChase(strip, Color(127, 127, 127))  # White theater chase
	theaterChase(strip, Color(127,   0,   0))  # Red theater chase
	theaterChase(strip, Color(  0,   0, 127))  # Blue theater chase
	# Rainbow animations.
	rainbow(strip)
	rainbowCycle(strip)
	theaterChaseRainbow(strip)