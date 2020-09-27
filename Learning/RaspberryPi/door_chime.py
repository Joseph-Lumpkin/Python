# import RPi.GPIO as GPIO
import time
import pyaudio
import wave
import sys

# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(7, GPIO.IN)

CHUNK = 1024
wf = wave.open(sys.argv[1], 'rb')

p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

data = wf.readframes(CHUNK)

while data != '':
    stream.write(data)
    data = wf.readframes(CHUNK)

stream.stop_stream()
stream.close()

p.terminate()

#time.sleep(10)

# try:
#     while True:
#         if GPIO.input(7) == True:
#             print("input = true")
#             pygame.mixer.music.stop()
#         elif GPIO.input(7) == False:
#             pygame.mixer.Sound.play(door_chime)
#             print("input = false, music should be playing")

#         time.sleep(5)
# finally:
#     GPIO.cleanup()