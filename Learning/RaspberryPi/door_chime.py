import RPi.GPIO as GPIO
import time
import pygame

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)
pygame.mixer.init()
pygame.mixer.music.load('res/renai_circulation.mp3')

try:
    while True:
        if GPIO.input(7):
            print("input = true")
            pygame.mixer.music.stop
            continue
        if GPIO.input(7) == False:
            print("input = false, music should be playing")
            if pygame.mixer.music.get_busy() == True:
                continue
            pygame.mixer.music.play()
finally:
    GPIO.cleanup()