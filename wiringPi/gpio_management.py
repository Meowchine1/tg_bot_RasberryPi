
#import RPi.GPIO as GPIO
import time
 
from wiringPi.config import *
from app_api import *

# #----------------------SETTING UP------------------------------------
# # Делаем сброс состояний портов (все конфигурируются на вход - INPUT)
# GPIO.cleanup()
# # Режим нумерации пинов - по названию (не по порядковому номеру на разъеме)
# GPIO.setmode(GPIO.BCM)

# GPIO.setup(SYGNAL, GPIO.IN)
# GPIO.setup(LED1, GPIO.OUT)
# GPIO.setup(LED2, GPIO.OUT)
# GPIO.setup(LED3, GPIO.OUT)
# GPIO.setup(RELE, GPIO.OUT)

# GPIO.output(LED1, GPIO.LOW)
# GPIO.output(LED2, GPIO.LOW)
# GPIO.output(LED3, GPIO.LOW)
# GPIO.output(RELE, GPIO.LOW)


def set_mode1():
    set_state(State.MODE1)
    led_st = set_led1_state(GPIO.HIGH)
    GPIO.output(LED1, led_st)

def set_mode2():
    set_state(State.MODE2) 
    set_rele_state(GPIO.HIGH) 
    led_st = set_led2_state(GPIO.HIGH)
    GPIO.OUT(LED2, led_st) 
    set_mode2_start_time(time.time()) 

def set_mode3():
    set_state(State.MODE3) 
    set_rele_state(GPIO.HIGH)
    led_st1 = set_led1_state(GPIO.HIGH) 
    led_st3 = set_led3_state(GPIO.HIGH)
    GPIO.OUT(LED1, led_st1) 
    GPIO.OUT(LED3, led_st3) 
   
def set_releoff():
    set_state(State.RELEOFF) 
    set_rele_state(GPIO.LOW)
    led_st3 = set_led3_state(GPIO.HIGH)
    GPIO.OUT(LED3, led_st3) 

def turnoff_mode1():
    led_st1 = set_led1_state(GPIO.LOW) 
    GPIO.OUT(LED1, led_st1) 

def turnoff_mode2():
    led_st = set_led2_state(GPIO.LOW) 
    GPIO.OUT(LED2, led_st) 

def turnoff_mode3():
    led_st1 = set_led1_state(GPIO.LOW)
    led_st3 = set_led3_state(GPIO.LOW) 
    GPIO.OUT(LED1, led_st1) 
    GPIO.OUT(LED3, led_st3) 

def turnoff_releoff():
    led_st3 = set_led3_state(GPIO.LOW)
    GPIO.OUT(LED3, led_st3)
    

def blink_1_3():
    led1_state = set_led1_state(~get_led1_state())
    led3_state = set_led3_state(~get_led3_state())

    GPIO.OUT(LED1, led1_state)
    GPIO.OUT(LED3, led3_state)    

