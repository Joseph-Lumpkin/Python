import RPi.GPIO as GPIO
import time
import pygame

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)
pygame.mixer.init()
pygame.mixer.music.load('renai_circulation.mp3')

try:
    while True:
        if GPIO.input(7):
            pygame.mixer.music.stop
            continue
        if GPIO.input(7) == False:
            if pygame.mixer.music.get_busy() == True:
                continue
            pygame.mixer.music.play()
finally:
    GPIO.cleanup()