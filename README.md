![Newpaltz Logo](http://www.newpaltz.edu/media/identity/logos/newpaltzlogo.jpg)

# Spring 2020 Embedded Linux Class.

The smoke detector is always running in the background and uses an sql database to log detected states (0) and undetected states (1) and upload them to a web page using a flask server.
The sql database is updated every 10 seconds, and the webpage updates automatically every 30 seconds.
Sensors used include the MQ-2 Sensor, the MQ-5 Sensor, the MQ-7 Sensor, The Flame Sensor, and the Buzzer Alarm Sensor.
This project uses the digital output (DO) on each of the sensors and will not require the use of an anaglog-digital convertor.
This script uses Python 3 and Flask.

Wire each sensor using 3.3v output from the Raspberry Pi

Two photos of my breadboard are shown in this repository

MQ-2 Pin = 13
MQ-5 Pin = 19
MQ-7 Pin = 26
Buzzer Alarm Sensor Pin = 21
Flame Sensor Pin = 12
