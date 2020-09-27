import RPi.GPIO as GPIO
import pygame
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)
pygame.mixer.init()
pygame.mixer.music.load("renai_circulation.mp3")

try:
    while True:
        if GPIO.input(7) == False:
            print("Door Closed = true, stopping music")
            pygame.mixer.music.stop()
        elif GPIO.input(7) == True:
            if pygame.mixer.music.get_busy() == False:
                pygame.mixer.music.stop()
                pygame.mixer.music.load("renai_circulation.mp3")
                pygame.mixer.music.play()
                print("Door Closed = false (door is open), playing music")
        time.sleep(.5)
finally:
    GPIO.cleanup()