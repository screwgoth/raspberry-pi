import RPi.GPIO as GPIO
import dht11
import time
import datetime

# initialize GPIO
port = 22
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

GPIO.setup(port, GPIO.IN)

def callback(port):
    if GPIO.input(port):
        print "Sound detected - High"
    else:
        print "Sound detected - Low"

GPIO.add_event_detect(port, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(port, callback)


while True:
    time.sleep(1)
