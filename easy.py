#!/usr/bin/python

import random
from random import choice
import subprocess
import CHIP_IO.GPIO as GPIO
from flask import Flask, request, render_template
app = Flask(__name__)
 
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    button_name = text.upper()
    return ("Your new button is named %s.") % button_name
    time.sleep(2)
    return render_template('buttonsetup.html')

#Sets up CSID0 as input for button
GPIO.setup("CSID0", GPIO.IN)

wavs = open('wavs.txt').read().splitlines()
print(wavs)

#Runs infinitely
while True:
  #If button pressed
  if GPIO.input("CSID0"):
    wav = random.choice(wavs)
    wav = wav.strip('\n')
    subprocess.call(['play', wav])

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
