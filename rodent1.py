import RPi.GPIO as GPIO
import time
import datetime
from datetime import datetime
from gpiozero import CPUTemperature

GPIO.setmode(GPIO.BCM)
PIR_PIN=7
GPIO.setup(PIR_PIN, GPIO.IN)

# CPU temperature object containing current CPU temp.
cpu = CPUTemperature()

# PIR Sensor
try:
  print ("PIR Module Test (CTRL+C)")
  time.sleep(2)
  print ("Ready")
  while True:
    if GPIO.input(PIR_PIN):
      # Datetime object containg current date and time
      now = datetime.now()
      dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
      print ("Motion Detected!",dt_string)
      print ("CPU temp is",cpu.temperature,"Degrees C")
    time.sleep(2) 

 except KeyboardInterrupt:
     print ("Quit")
     GPIO.cleanup()
