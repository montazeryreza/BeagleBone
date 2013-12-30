# Program to control a unipolar stepper motor
# Created by Nitesh Kadyan on 30/12/2013 (dd/mm/yyyy)
# https://www.youtube.com/watch?v=dEDHyxoFSLw
# This program is in public domain.

import Adafruit_BBIO.GPIO as GPIO
import time

GPIO.setup("P8_7", GPIO.OUT)
GPIO.setup("P8_8", GPIO.OUT)
GPIO.setup("P8_9", GPIO.OUT)
GPIO.setup("P8_10", GPIO.OUT)

a = 0

def rotateClockWise(steps, off_time):

	global a
	
	for i in range(0, steps):
		a = a + 1
		b = 1 + (abs(a) % 4)

		if a < 0:
			b = 5 - b;

		if b == 1:
			GPIO.output("P8_9", GPIO.LOW)
			GPIO.output("P8_8", GPIO.LOW)
			GPIO.output("P8_10", GPIO.LOW)
			GPIO.output("P8_7", GPIO.HIGH)

		if b == 2:
        	        GPIO.output("P8_7", GPIO.LOW)
                	GPIO.output("P8_8", GPIO.LOW)
	                GPIO.output("P8_10", GPIO.LOW)
        	        GPIO.output("P8_9", GPIO.HIGH)

		if b == 3:
        	        GPIO.output("P8_7", GPIO.LOW)
                	GPIO.output("P8_9", GPIO.LOW)
	                GPIO.output("P8_10", GPIO.LOW)
        	        GPIO.output("P8_8", GPIO.HIGH)

		if b == 4:
        	        GPIO.output("P8_7", GPIO.LOW)
                	GPIO.output("P8_9", GPIO.LOW)
	                GPIO.output("P8_8", GPIO.LOW)
        	        GPIO.output("P8_10", GPIO.HIGH)

		time.sleep(off_time)


def rotateCounterClockWise(steps, off_time):

	global a

        for i in range(0, steps):
                a = a - 1
                b = 1 + (abs(a) % 4)

                if a < 0:
                        b = 5 - b;

                if b == 4:
                        GPIO.output("P8_7", GPIO.LOW)
                        GPIO.output("P8_9", GPIO.LOW)
                        GPIO.output("P8_8", GPIO.LOW)
                        GPIO.output("P8_10", GPIO.HIGH)

                if b == 3:
                        GPIO.output("P8_7", GPIO.LOW)
                        GPIO.output("P8_9", GPIO.LOW)
                        GPIO.output("P8_10", GPIO.LOW)
                        GPIO.output("P8_8", GPIO.HIGH)

                if b == 2:
			GPIO.output("P8_7", GPIO.LOW)
                        GPIO.output("P8_8", GPIO.LOW)
                        GPIO.output("P8_10", GPIO.LOW)
                        GPIO.output("P8_9", GPIO.HIGH)

		if b == 1:
                        GPIO.output("P8_9", GPIO.LOW)
                        GPIO.output("P8_8", GPIO.LOW)
                        GPIO.output("P8_10", GPIO.LOW)
                        GPIO.output("P8_7", GPIO.HIGH)

		time.sleep(off_time)

def main():
	while True:
        	rotateClockWise(200, 0.003)
	        time.sleep(1)
		rotateCounterClockWise(200, 0.003)
		time.sleep(1)

if __name__ == "__main__":
    main()
