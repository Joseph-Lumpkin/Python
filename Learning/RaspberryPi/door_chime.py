import RPi.GPIO as GPIO
import pygame
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)
GPIO.setup(37, GPIO.IN)

pygame.mixer.init()
pygame.mixer.music.load("renai_circulation.mp3")

try:
    while True:
        if GPIO.input(7) == True:
            if GPIO.input(37) == True:
                print("Door Closed = true, stopping music")
                pygame.mixer.music.stop()
        if GPIO.input(7) == False:
            if GPIO.input(37) == False:
                if pygame.mixer.music.get_busy() == False:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("renai_circulation.mp3")
                    pygame.mixer.music.play()
                    print("Door Closed = false (door is open), playing music")
        time.sleep(1)
finally:
    GPIO.cleanup()