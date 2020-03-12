#Import libraries
import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import os
import sqlite3 as mydb

con = None

con = mydb.connect('../log/tempLog.db')
cur = con.cursor()

eChk = 0

#Assign Pins
redPin = 27
greenPin = 22
tempPin = 17
#touchPin = 26

tempSensor = Adafruit_DHT.DHT11

#LED variables
blinkDur = .1
blinkTime = 7

#Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(redPin,GPIO.OUT)
GPIO.setup(greenPin,GPIO.OUT)
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
		humidity = '{0:0.1f}'.format(humidity)
	else:
		print('Error Reading Sensor')

	return tempFahr, humidity

#First iteration of loop
oldTime = 60

tempF, humid = readF(tempPin)


try:

	while True:

		#if 68 <= float(tempF) <= 78:
			#eChk = 0
			#GPIO.output(redPin.False)
			#GPIO.output(greenPin.True)
		#else:
			#GPIO.output(greenPin.False)
			#oneBlink(redPin)
		if(time.time() - oldTime) > 59:
			tempF, humid = readF(tempPin)
			#Defines and executes sql query
			cur.execute('INSERT INTO tempLog values(?,?,?)', (time.strftime('%Y-%m-%d %H:%M:%S'),tempF,humid))
			con.commit()
			#time.sleep(5)

			table = con.execute("select * from tempLog")
			os.system('clear')
			print "%-30s %-20s %-20s" %("Date/Time", "Temp", "Humidity")
			for row in table:
				print "%-30s %-20s %-20s" %(row[0], row[1], row[2])
			oldTime = time.time()

#Cleanup the GPIO when done
except KeyboardInterrupt:
	os.system('clear')
	con.close()
	GPIO.cleanup()
	print("Clear")
