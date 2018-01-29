import random
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

#Runs infinitely
while True:
  #If button pressed
  wav = random.choice(list(open('wavs.txt')))
  if GPIO.input("CSID0"):
    subprocess.call(['play', '%s'] % wav)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
