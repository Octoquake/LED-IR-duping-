import RPi.GPIO as GPIO
import fileinput
from time import sleep
import time
import datetime
#;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
#GPIO Settings
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
#;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
#Main Code
while True:
	##START BIT
	GPIO.output(26, 0)
	sleep(0.009)
	GPIO.output(26, 1)
	sleep(0.0045)
	
	##ADDRESS
	address = "0000000011111111"

	for digit in address:
		GPIO.output(26, 0)
		sleep(0.00056)
		GPIO.output(26, 1)
		if int(digit):
			sleep(0.00169)
		else:
			sleep(0.00056)

	##COMMAND
	command = "0101000010101111"

	for digit in command:
		GPIO.output(26, 0)
		sleep(0.00056)
		GPIO.output(26, 1)
		if int(digit):
			sleep(0.00169)
		else:
			sleep(0.00056)
	
	##STOP BIT
	GPIO.output(26, 0)
	sleep(0.009)
	GPIO.output(26, 1)
	sleep(0.0045)

	print('diy6')
	break
#;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
