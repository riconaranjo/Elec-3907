
max_x_limit = 250
max_y_limit = 255
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

def XledOn(x):

	if x < max_x_limit/4 and x > 0:
		GPIO.output(26,GPIO.HIGH)
		GPIO.output(4,GPIO.HIGH)
		
		
	if x < max_x_limit/2 and x > max_x_limit/4:
		GPIO.output(4,GPIO.HIGH)
		GPIO.output(17,GPIO.HIGH)
		
		
	if x < 3*max_x_limit/4 and x>2*max_x_limit/4:
		GPIO.output(17,GPIO.HIGH)
		GPIO.output(27,GPIO.HIGH)
		
		
	if x < max_x_limit and x > 3*max_x_limit/4:
		GPIO.output(27,GPIO.HIGH)
		GPIO.output(22,GPIO.HIGH)
		
		
def XledOff(x):

    if x < max_x_limit/4 and x > 0:
        GPIO.output(26,GPIO.LOW)
        GPIO.output(4,GPIO.LOW)
	
    if x < max_x_limit/2 and x > max_x_limit/4:
        GPIO.output(4,GPIO.LOW)
        GPIO.output(17,GPIO.LOW)
    if x < 3*max_x_limit/4 and x>2*max_x_limit/4:
        GPIO.output(17,GPIO.LOW)
        GPIO.output(27,GPIO.LOW)
	
    if x < max_x_limit  and x > 3*max_x_limit/4:
        GPIO.output(27,GPIO.LOW)
        GPIO.output(22,GPIO.LOW)
        
def YledOn(y):

    if y < max_y_limit/4 and y > 0:
        GPIO.output(26,GPIO.HIGH)
        GPIO.output(5,GPIO.HIGH)
		
    if y < max_y_limit/2 and y > max_y_limit/4:
        GPIO.output(5,GPIO.HIGH)
        GPIO.output(6,GPIO.HIGH)
		
		
    if y < 3*max_y_limit/4 and y > 2*max_y_limit/4:
        GPIO.output(6,GPIO.HIGH)
        GPIO.output(13,GPIO.HIGH)
		
		
    if y < max_y_limit and y > 3*max_y_limit/4:
        GPIO.output(13,GPIO.HIGH)
        GPIO.output(19,GPIO.HIGH)
		
		
def YledOff(y):
    if y < max_y_limit/4 and y > 0:
        GPIO.output(26,GPIO.LOW)
        GPIO.output(5,GPIO.LOW)
	
    if y < max_y_limit/2 and y > max_y_limit/4:
        GPIO.output(5,GPIO.LOW)
        GPIO.output(6,GPIO.LOW)
	
    if y < 3*max_y_limit/4 and y > 2*max_y_limit/4:
        GPIO.output(6,GPIO.LOW)
        GPIO.output(13,GPIO.LOW)
		
    if y < max_y_limit and y > 3*max_y_limit/4:
        GPIO.output(13,GPIO.LOW)
        GPIO.output(19,GPIO.LOW)
        
def leds(x,y):
    XledOn(float(x))
    YledOn(float(y))
    time.sleep(0.2)
    XledOff(float(x))
    YledOff(float(y))
def ledsOff():
    GPIO.output(13,GPIO.LOW)
    GPIO.output(19,GPIO.LOW)
    GPIO.output(5,GPIO.LOW)
    GPIO.output(6,GPIO.LOW)
    GPIO.output(27,GPIO.LOW)
    GPIO.output(22,GPIO.LOW)
    GPIO.output(4,GPIO.LOW)
    GPIO.output(17,GPIO.LOW)
    GPIO.output(26,GPIO.LOW)
    
ledsOff()
f=open('test_numbers.txt')
for line in f:
    
   
  x,y = line.split(" ")
  print("x,y = {},{}".format(x,y))
  
  leds(x,y)
  
ledsOff()
  