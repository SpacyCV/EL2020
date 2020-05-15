Directory for storing code used for the project. Note that the sql database is stored in the log directory
The smoke.py script should be used in screen (run with command "screen -S detector). This code listens for detections from each of the sensors and logs values to an SQL Database (smoke.db)
flaskServer.py is the script that runs the server used for viewing the detection state of the sensors connected to the Pi. It calls the index.html file stored in the templates directory, and retrieves the data from smoke.db to display on the web page, which updates automatically every 30 seconds.

the buzzer.py script is only used to test the buzzer alarm module once it is wired to the Pi.
