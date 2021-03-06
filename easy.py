#!/usr/bin/python

import random
from random import choice
import subprocess
import CHIP_IO.GPIO as GPIO
GPIO.setup("CSID0", GPIO.IN)

wavs = open('wavs.txt').read().splitlines()
print(wavs)

#Runs infinitely
def button():
  while True:
    #If button pressed
    if GPIO.input("CSID0"):
      wav = random.choice(wavs)
      wav = wav.strip('\n')
      subprocess.call(['play', wav])

if __name__ == "__main__":
  button()
