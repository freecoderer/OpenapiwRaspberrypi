
import RPi.GPIO as GPIO

import time

from pyowm import OWM

​

GPIO.setmode(GPIO.BOARD)

fan = 3

GPIO.setup(fan, GPIO.OUT)

GPIO.setwarnings(False)

p = GPIO.PWM(fan, 100)

p.start(100)
