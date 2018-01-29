import subprocess
import CHIP_IO.GPIO as GPIO

#Sets up CSID0 as input for button
GPIO.setup("CSID0", GPIO.IN)

#Runs infinitely
while True:
  #If button pressed
  if GPIO.input("CSID0"):
    subprocess.call(['play', 'easy.wav'])
