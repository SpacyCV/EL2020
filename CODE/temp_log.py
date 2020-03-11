#Import libraries
import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import os
import sqlite3 as mydb

con = None

try:
	con = mydb.connect('../log/tempLog.db')
	cur = con.cursor()
	cur.execute('SELECT SQLITE_VERSION()')
except mydb.Error, e:
	print "Error %s:" % e.args[0]
	exit()

#Assign Pins
lightPin = 27
tempPin = 17
#touchPin = 26

tempSensor = Adafruit_DHT.DHT11

#LED variables
blinkDur = .1
blinkTime = 7

#Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(lightPin,GPIO.OUT)
#GPIO.setup(touchPin,GPIO.IN)


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
		tempFahr = '{0:0.1f}'.format(temperature)
		humidity = '{0:0.1f}%'.format(humidity)
	else:
		print('Error Reading Sensor')

	return tempFahr,humidity

try:
	with open("../log/tempLog.csv", "a") as log:

		while True:
			#input_state = GPIO.input(touchPin)
			#if input_state == True:
			for i in range (blinkTime):
				blinkOnce(lightPin)
			time.sleep(.2)
			temp, humidity = readF(tempPin)
			print (temp)
			#log.write("{0},{1},{2}\n".format(time.strftime("%Y-%m-%d,%H:%M:%S"),str(temp),str(humidity)))
			date = time.strftime("%Y-%m-%d")
			time = time.strftime("%H:%M:%S")
			cur.execute("INSERT INTO tempLog VALUES (str(date),str(time),str(temp),str(humidity))")
			time.sleep(58)

#Cleanup the GPIO when done
except KeyboardInterrupt:
	os.system('clear')
	con.commit()
	con.close()
	GPIO.cleanup()
	print("Clear")
