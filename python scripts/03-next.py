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
#Variables
##START 
##	GPIO.output(26, 0)
##	sleep(0.009)
##	GPIO.output(26, 1)
##	sleep(0.0045)

##0BIT
##	GPIO.output(26, 0)
##	sleep(0.00056)
##	GPIO.output(26, 1)
##	sleep(0.00056)

##1BIT
##	GPIO.output(26, 0)
##	sleep(0.00056)
##	GPIO.output(26, 1)
##	sleep(0.00169)

##STOP
##	GPIO.output(26, 0)
##	sleep(0.009)
##	GPIO.output(26, 1)
##	sleep(0.0045)

#;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
#Main Code
while True:
	##START BIT
	GPIO.output(26, 0)
	sleep(0.009)
	GPIO.output(26, 1)
	sleep(0.0045)
	
	##ADDRESS 00000000
	GPIO.output(26, 0)
	sleep(0.00056)
	GPIO.output(26, 1)
	sleep(0.00056)

	GPIO.output(26, 0)
	sleep(0.00056)
	GPIO.output(26, 1)
	sleep(0.00056)

	GPIO.output(26, 0)
	sleep(0.00056)
	GPIO.output(26, 1)
	sleep(0.00056)

	GPIO.output(26, 0)
	sleep(0.00056)
	GPIO.output(26, 1)
	sleep(0.00056)

	GPIO.output(26, 0)
	sleep(0.00056)
	GPIO.output(26, 1)
	sleep(0.00056)

	GPIO.output(26, 0)
	sleep(0.00056)
	GPIO.output(26, 1)
	sleep(0.00056)

	GPIO.output(26, 0)
	sleep(0.00056)
	GPIO.output(26, 1)
	sleep(0.00056)

	GPIO.output(26, 0)
	sleep(0.00056)
	GPIO.output(26, 1)
	sleep(0.00056)

	##INVERT ADDRESS 11111111
	GPIO.output(26, 0)
	sleep(0.00056)
	GPIO.output(26, 1)
	sleep(0.00169)

	GPIO.output(26, 0)
	sleep(0.00056)
	GPIO.output(26, 1)
	sleep(0.00169)

	GPIO.output(26, 0)
	sleep(0.00056)
	GPIO.output(26, 1)
	sleep(0.00169)

	GPIO.output(26, 0)
	sleep(0.00056)
	GPIO.output(26, 1)
	sleep(0.00169)

	GPIO.output(26, 0)
	sleep(0.00056)
	GPIO.output(26, 1)
	sleep(0.00169)

	GPIO.output(26, 0)
	sleep(0.00056)
	GPIO.output(26, 1)
	sleep(0.00169)

	GPIO.output(26, 0)
	sleep(0.00056)
	GPIO.output(26, 1)
	sleep(0.00169)

	GPIO.output(26, 0)
	sleep(0.00056)
	GPIO.output(26, 1)
	sleep(0.00169)

#;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
	##COMMAND 10000010
	GPIO.output(26, 0)
	sleep(0.00056)
	GPIO.output(26, 1)
	sleep(0.00169)

	GPIO.output(26, 0)
	sleep(0.00056)
	GPIO.output(26, 1)
	sleep(0.00056)

	GPIO.output(26, 0)
	sleep(0.00056)
	GPIO.output(26, 1)
	sleep(0.00056)	

	GPIO.output(26, 0)
	sleep(0.00056)
	GPIO.output(26, 1)
	sleep(0.00056)

	GPIO.output(26, 0)
	sleep(0.00056)
	GPIO.output(26, 1)
	sleep(0.00056)

	GPIO.output(26, 0)
	sleep(0.00056)
	GPIO.output(26, 1)
	sleep(0.00056)

	GPIO.output(26, 0)
	sleep(0.00056)
	GPIO.output(26, 1)
	sleep(0.00169)

	GPIO.output(26, 0)
	sleep(0.00056)
	GPIO.output(26, 1)
	sleep(0.00056)

	##INVERT COMMAND 01111101
	GPIO.output(26, 0)
	sleep(0.00056)
	GPIO.output(26, 1)
	sleep(0.00056)

	GPIO.output(26, 0)
	sleep(0.00056)
	GPIO.output(26, 1)
	sleep(0.00169)

	GPIO.output(26, 0)
	sleep(0.00056)
	GPIO.output(26, 1)
	sleep(0.00169)	

	GPIO.output(26, 0)
	sleep(0.00056)
	GPIO.output(26, 1)
	sleep(0.00169)

	GPIO.output(26, 0)
	sleep(0.00056)
	GPIO.output(26, 1)
	sleep(0.00169)

	GPIO.output(26, 0)
	sleep(0.00056)
	GPIO.output(26, 1)
	sleep(0.00169)

	GPIO.output(26, 0)
	sleep(0.00056)
	GPIO.output(26, 1)
	sleep(0.00056)

	GPIO.output(26, 0)
	sleep(0.00056)
	GPIO.output(26, 1)
	sleep(0.00169)
	
#;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
	##STOP BIT
	GPIO.output(26, 0)
	sleep(0.009)
	GPIO.output(26, 1)
	sleep(0.0045)	
		
	print('next')
	break
#;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;