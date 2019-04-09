#!/usr/bin/python

import sys
import time
import datetime#!/usr/bin/python

import sys
import time
import datetime
MyDateTime = datetime.datetime.now()

from sense_hat import SenseHat
sense = SenseHat()
sense.clear()

import Adafruit_DHT
Date = MyDateTime.strftime("%m/%d/%y")
Time = MyDateTime.strftime("%H:%M:%S")

from time import sleep

sensor_args = {'2302': Adafruit_DHT.AM2302 }

if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
	sensor = sensor_args[sys.argv[1]]
	pin = sys.argv[2]
	sense.show_message("READY!", text_colour=(76, 187, 23))
else:
	print('usage: sudo ./Adafruit_DHT.py [11|22|2302] GPIOpin#')
	print('example: sudo ./Adafruit_DHT.py 2302 4 - Read from an AM2302 connected to GPIO #4')
	sense.show_message("ERROR!", text_colour=(255, 0, 0))
	sys.exit(1)

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
temperature = temperature * 9/5.0 + 32

csvresult = open("/home/pi/Desktop/SpaceBalloonLog.csv","a")
csvresult.write("Log #" + "," + "Date" + "," "Time" + "," "Temperature (*F)" + "," "Humidity (%)" + "," "Pressure" + "," "Internal Temperature (*F)" + "," "Internal Humidity (%)" + "\n")
csvresult.close

Count = 1
while(Count < 99999):
	import time
	import datetime
	MyDateTime = datetime.datetime.now()
	Date = MyDateTime.strftime("%m/%d/%y")
	Time = MyDateTime.strftime("%H:%M:%S")
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	temperature = temperature * 9/5.0 + 32

	pressure = sense.get_pressure()
	pressure = round(pressure, 2)
	humidin = sense.get_humidity()
	humidin = round(humidin, 2)
	tempin = sense.get_temperature_from_pressure()
	tempinf = tempin * 9/5.0 + 32
	tempinf = round(tempinf, 2)

	sleep(2)

	csvresult = open("/home/pi/Desktop/SpaceBalloonLog.csv","a")
	csvresult.write(('{}'.format(Count)) + "," + Date + "," + Time + "," + ('{0:0.1f}, {1:0.1f}'.format(temperature, humidity)) + "," + str(pressure) + "," + str(tempinf) + "," + str(humidin) + "," "\n")
	csvresult.close
	print("Data Logged")
	sense.set_pixel(0, 0, 76, 187, 23)
	time.sleep(1)
	sense.set_pixel(0, 0, 0, 0, 0)
	time.sleep(26)
	Count = Count + 1

sense.show_message("LOOP ERROR!  LOOP ERROR!", text_colour=(255, 0, 0))	
