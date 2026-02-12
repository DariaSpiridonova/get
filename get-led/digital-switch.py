import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led = 26

GPIO.setup(led, GPIO.OUT)

botton = 13

GPIO.setup(botton, GPIO.IN)

state = 0
period = 2.0

while True:
    if GPIO.input(button):
        state = not state
        GPIO.output(led, state)
        time.sleep(period)