#!/usr/bin/python

import random
from random import choice
import subprocess
import CHIP_IO.GPIO as GPIO
from flask import Flask, request, render_template
app = Flask(__name__)
GPIO.setup("CSID0", GPIO.IN)
button_name = ""

@app.route("/")
def index():
    return render_template('index.html')

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
  app.run(debug=True, host='0.0.0.0')
  button()
