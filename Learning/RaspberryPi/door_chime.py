import RPi.GPIO as GPIO
import time
import playsound

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)


try:
    while True:
        if GPIO.input(7):
            continue
        if GPIO.input(7) == False:
            playsound('res/renai_circulation')
        time.sleep(10);
finally:
    GPIO.cleanup()