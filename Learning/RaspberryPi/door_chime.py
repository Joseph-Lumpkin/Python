import RPi.GPIO as GPIO
import pygame
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)
pygame.mixer.init()
pygame.mixer.music.load("res/music/cyka.mp3")

try:
    while True:
        if GPIO.input(7) == True:
            print("input = true")
            pygame.mixer.music.stop()
        elif GPIO.input(7) == False:
            if pygame.mixer.music.get_busy() == False:
                pygame.mixer.music.stop()
                pygame.mixer.music.load("res/music/cyka.mp3")
                pygame.mixer.music.play()
                print("input = false, music should be playing")
        time.sleep(.5)
finally:
    GPIO.cleanup()