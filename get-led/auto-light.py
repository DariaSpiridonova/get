import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led = 26

GPIO.setup(led, GPIO.OUT)

div_u = 6
GPIO.setup(div_u, GPIO.IN)

while True:
    div_u = not div_u
    GPIO.output(led, div_u)
    time.sleep(2.0)
