import RPi.GPIO as GPIO
import time
from wiringPi.config import *
from app_api import *

def current_milli_time():
    return round(time.time() * 1000)

#----------------------SETTING UP------------------------------------
# # Делаем сброс состояний портов (все конфигурируются на вход - INPUT)
# GPIO.cleanup()


# Режим нумерации пинов - по названию (не по порядковому номеру на разъеме)

GPIO.setmode(GPIO.BCM)
GPIO.setup(SYGNAL, GPIO.IN)
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)
GPIO.setup(RELE, GPIO.OUT)
GPIO.output(LED1, 0)
GPIO.output(LED2, 0)
GPIO.output(LED3, 0)
GPIO.output(RELE, 0)


def set_mode1():
    led_st = set_led1_state(1)
    GPIO.output(LED1, led_st)
    set_state(State.MODE1)

def set_mode2():
    set_mode2_start_time(current_milli_time())
    set_rele_state(1) 
    led_st = set_led2_state(1)
    GPIO.output(LED2, led_st) 
    set_state(State.MODE2) 

def set_mode3(): 
    set_rele_state(1)
    led_st1 = set_led1_state(1) 
    led_st3 = set_led3_state(1)
    GPIO.output(LED1, led_st1) 
    GPIO.output(LED3, led_st3) 
    set_state(State.MODE3)
    
def set_releoff():
    set_rele_state(0)
    led_st3 = set_led3_state(1)
    GPIO.output(LED3, led_st3)
    set_state(State.RELEOFF) 

def turnoff_mode1():
    led_st1 = set_led1_state(0) 
    GPIO.output(LED1, led_st1) 

def turnoff_mode2():
    led_st = set_led2_state(0) 
    GPIO.output(LED2, led_st) 

def turnoff_mode3():
    led_st1 = set_led1_state(0)
    led_st3 = set_led3_state(0) 
    GPIO.output(LED1, led_st1) 
    GPIO.output(LED3, led_st3) 

def turnoff_releoff():
    led_st3 = set_led3_state(0)
    GPIO.output(LED3, led_st3)
    

def blink_1_3():
    led1_state = set_led1_state(not get_led1_state())
    print(f"led1_state = {led1_state}")
    led3_state = set_led3_state(not get_led3_state())

    GPIO.output(LED1, led1_state)
    GPIO.output(LED3, led3_state)    

