import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [16, 12, 25, 17, 27, 23, 22, 24]

GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)

light_time = 0.2

button_up = 9
button_down = 10

GPIO.setup(button_up, GPIO.IN)
GPIO.setup(button_down, GPIO.IN)

num = 0

sleep_time = 0.2
max_num = 255

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

while True:
    if GPIO.input(button_up) > 0:
        if num < max_num:
            num += 1
        else:
            num = 0
        print(num, dec2bin(num))
        GPIO.output(leds, dec2bin(num))
        time.sleep(sleep_time)

    if GPIO.input(button_down) > 0:
        if num > 0:
            num -= 1
        print(num, dec2bin(num))
        GPIO.output(leds, dec2bin(num))
        time.sleep(sleep_time)