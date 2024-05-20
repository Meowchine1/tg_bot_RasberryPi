
import RPi.GPIO as GPIO

import time
from enum import Enum

#include <wiringPi.h> # Include WiringPi library!

#----------------------LEDS----------------------
LED1 = 26 #  37 # 26 
LED2 = 19 # 35 # 19 
LED3 = 13 #33 # 13
RELE = 16 #31 # 16
SYGNAL = 5 #29 # 5

led1_state = GPIO.HIGH
led2_state = GPIO.LOW
led3_state = GPIO.LOW
rele_state = GPIO.LOW

BLINK_INTERVAL = 500
previousMillis = 0

# ----------------------MODE VARIABLES--------------------------------

class State(enum.Enum):
    MODE1 = 0   # штатный режим, при прерывании сигнала переход в режим отключенного реле
    MODE2 = 1  # режим без прерывания реле при прекращении сигнала (ограниченное время)
    MODE3 = 2  # режим без прерывания реле при прекращении сигнала (неограниченное время)
    RELEOFF = 3 # режим отключенного реле

state = State.MODE1

#  MODE2 TIMER
mode2_start_time = 0
MODE2_INTERVAL = 300000

def set_mode1():
    state = State.MODE1
    led1_state = GPIO.HIGH
    GPIO.output(LED1, led1_state)

def set_mode2():
    state = State.MODE2 
    rele_state = GPIO.HIGH 
    led2_state = GPIO.HIGH
    GPIO.OUT(LED2, led2_state) 
    mode2_start_time = time.time() 

def set_mode3():
    state = State.MODE3 
    rele_state = GPIO.HIGH
    led1_state = GPIO.HIGH 
    led3_state = GPIO.HIGH
    GPIO.OUT(LED1, led1_state) 
    GPIO.OUT(LED3, led3_state) 
   

def set_releoff():
    state = State.RELEOFF 
    rele_state = GPIO.LOW 
    led3_state = GPIO.HIGH
    GPIO.OUT(LED3, led3_state) 

def turnoff_mode1():
    led1_state = GPIO.LOW 
    GPIO.OUT(LED1, led1_state) 


def turnoff_mode2():
    led2_state = GPIO.LOW 
    GPIO.OUT(LED2, led2_state) 


def turnoff_mode3():
    led1_state = GPIO.LOW
    led3_state = GPIO.LOW 
    GPIO.OUT(LED1, led1_state) 
    GPIO.OUT(LED3, led3_state) 


def turnoff_releoff():
    led3_state = GPIO.LOW
    GPIO.OUT(LED3, led3_state) 

