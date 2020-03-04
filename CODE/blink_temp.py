#Import libraries
import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import os

#Assign Pins
lightPin = 27
tempPin = 17
touchPin = 26

tempSensor = Adafruit_DHT.DHT11

#LED variables
blinkDur = .1
blinkTime = 7

#Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(lightPin,GPIO.OUT)
GPIO.setup(touchPin,GPIO.IN)


#This function will make the light blink once
def blinkOnce(pin):
	GPIO.output(pin,True)
	time.sleep(blinkDur)
	GPIO.output(pin,False)
	time.sleep(blinkDur)

def readF(tempPin):
	humidity, temperature = Adafruit_DHT.read_retry(tempSensor,tempPin)
	temperature = temperature * 9/5.0 +32
	if humidity is not None and temperature is not None:
		tempFahr = '{0:0.1f}*F'.format(temperature)
	else:
		print('Error Reading Sensor')

	return tempFahr

try:
	while True:
		input_state = GPIO.input(touchPin)
		if input_state == True:
			for i in range (blinkTime):
				blinkOnce(lightPin)
			time.sleep(.2)
			data = readF(tempPin)
			print (data)

#Cleanup the GPIO when done
except KeyboardInterrupt:
	os.system('clear')
	GPIO.cleanup()
	print("Clear")
