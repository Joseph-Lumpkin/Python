import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.SETUP(7, GPIO.OUT)

for i in range(50):
    GPIO.output(7, True)
    time.sleep(.25)
    GPIO.output(7, False)
    time.sleep(.25)
    
GPIO.cleanup()