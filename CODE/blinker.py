#Import libraries
import RPi.GPIO as GPIO
import time
import os

#Initialize the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(26,GPIO.IN)

#This function will make the light blink once
def blinkOnce(pin):
	GPIO.output(pin,True)
	time.sleep(.1)
	GPIO.output(pin,False)
	time.sleep(.1)

#Call the blinkOnce function above in a loop
try:
	while True:
		input_state = GPIO.input(26)
		if input_state == True:
			blinkOnce(17)
		time.sleep(0.2)

#Cleanup the GPIO when done
except KeyboardInterrupt:
	os.system('clear')
	GPIO.cleanup()
	print("Clear")
