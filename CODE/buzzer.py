import time, sys
import RPi.GPIO as GPIO

#Pin for the MQ2 Smoke Detector
buzzerPin = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzerPin,GPIO.OUT)

try:
	while True:
		GPIO.output(buzzerPin,False)

except KeyboardInterrupt:
	GPIO.cleanup()
	sys.exit()
