import time, sys
import RPi.GPIO as GPIO
import sqlite3 as mydb

con = None

#Set pins
mq2Pin = 13
mq5Pin = 19
mq7Pin = 26
flamePin = 12
buzzerPin = 21

#Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(mq2Pin,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(mq5Pin,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(mq7Pin,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(flamePin,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(buzzerPin,GPIO.OUT)

#Set buzzer to inactive
GPIO.output(buzzerPin,True)

#If called, activates buzzer and adds 1 to sql db, signifying detection
def action(pin):
	GPIO.output(buzzerPin,False)
	log(1)
	time.sleep(10)
	return

#Logs values into sql db
def log(state):
	print(state)
	con = mydb.connect('../log/smoke.db')
	cur = con.cursor()
	cur.execute('INSERT INTO smoke values(?,?)', (time.strftime('%Y-%m-%d %H:%M:%S'),state))
	con.commit()
	return

#Set triggers for detection sensors
GPIO.add_event_detect(mq2Pin, GPIO.RISING)
GPIO.add_event_callback(mq2Pin, action)
GPIO.add_event_detect(mq5Pin, GPIO.RISING)
GPIO.add_event_callback(mq5Pin, action)
GPIO.add_event_detect(mq7Pin, GPIO.RISING)
GPIO.add_event_callback(mq7Pin, action)
GPIO.add_event_detect(flamePin, GPIO.RISING)
GPIO.add_event_callback(flamePin, action)

#Sets a while loop, checking the sensor every 10 seconds.
#If no smoke detected, add 0 to sql db, signifying no detection
try:
	while True:
		GPIO.output(buzzerPin,True)
		log(0)
		time.sleep(10)

except KeyboardInterrupt:
	time.sleep(3)
	GPIO.cleanup()
	sys.exit()
