import RPi.GPIO as GPIO
import time
import pygame

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)
pygame.init()

################
door_chime = pygame.mixer.Sound("res/renai_circulation.wav")
################

pygame.mixer.init()

try:
    while True:
        if GPIO.input(7) == True:
            print("input = true")
            pygame.mixer.music.stop()
        elif GPIO.input(7) == False:
            pygame.mixer.Sound.play(door_chime)
            print("input = false, music should be playing")

        time.sleep(5)
finally:
    GPIO.cleanup()