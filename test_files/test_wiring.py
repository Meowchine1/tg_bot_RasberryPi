import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.IN)
GPIO.setup(19, GPIO.OUT)

try:
    while 1:
        GPIO.output(19, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(19, GPIO.LOW)
except KeyboardInterrupt:
    GPIO.cleanup()
    print('interrupted!')        