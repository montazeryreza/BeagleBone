import Adafruit_BBIO.GPIO as GPIO
import time
 
GPIO.setup("P8_6", GPIO.OUT)
 
while True:
    GPIO.output("P8_6", GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output("P8_6", GPIO.LOW)
    time.sleep(0.5)
