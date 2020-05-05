import math
import sys
import time
from grove.adc import ADC
import RPi.GPIO as GPIO

#Initialize
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN)
GPIO.setup(27,GPIO.OUT)

