#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
GPIO.setmode(P|GPIO.BOARD)
GPIO.setup(22,GPIO.OUT)
while True:
  GPIO.output(22,True)
  time.sleep(2)
  GPIO.output(22,False)
  time.sleep(2)
