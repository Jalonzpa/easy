import random
import subprocess
import CHIP_IO.GPIO as GPIO
GPIO.setup("CSID0", GPIO.IN)

with open("wavs.txt") as file:
    for line in file:
        wavs = line.strip()
        wav = random.choice(wavs)

subprocess.call(['play', wav])
