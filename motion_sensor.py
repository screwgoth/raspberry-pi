import RPi.GPIO as GPIO
from time import sleep

#Use GPIO number instead of Pin number
#GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BOARD)
#Make GPIO 8 output
GPIO.setup(8, GPIO.IN)
GPIO.setup(22, GPIO.OUT)
GPIO.output(22, GPIO.LOW)
print "Waiting for sensor to settle"
sleep(3)
count = 0

try:
    while True:
            if GPIO.input(8):
                print "Motion detected..waiting for 3 secs. to stabilize"
                GPIO.output(22, GPIO.HIGH)
                sleep(0.5)
                sleep(2)
                GPIO.output(22, GPIO.LOW)
                sleep(0.5)
                count = 0
            else:
                count += 1
                print "No motion : %s"%(count)
            sleep(1)

#No error occurs when Ctrl+C is pushed.         
except KeyboardInterrupt:
    pass
    
#Release GPIO     
GPIO.cleanup()
