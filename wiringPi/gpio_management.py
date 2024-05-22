
import RPi.GPIO as GPIO
import time
from enum import Enum
from wiringPi.config import *
 


class State(Enum):
    MODE1 = 0   # штатный режим, при прерывании сигнала переход в режим отключенного реле
    MODE2 = 1  # режим без прерывания реле при прекращении сигнала (ограниченное время)
    MODE3 = 2  # режим без прерывания реле при прекращении сигнала (неограниченное время)
    RELEOFF = 3 # режим отключенного реле

class App:
    led1_state = GPIO.HIGH
    led2_state = GPIO.LOW
    led3_state = GPIO.LOW
    rele_state = GPIO.LOW
    mode2_start_time = 0
    previousMillis = 0
    state = State.MODE1
    
#----------------------SETTING UP------------------------------------
# Делаем сброс состояний портов (все конфигурируются на вход - INPUT)
GPIO.cleanup()
# Режим нумерации пинов - по названию (не по порядковому номеру на разъеме)
GPIO.setmode(GPIO.BCM)

GPIO.setup(SYGNAL, GPIO.IN)
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)
GPIO.setup(RELE, GPIO.OUT)

GPIO.output(LED1, GPIO.LOW)
GPIO.output(LED2, GPIO.LOW)
GPIO.output(LED3, GPIO.LOW)
GPIO.output(RELE, GPIO.LOW)


def set_mode1(obj : App):
    obj.state = State.MODE1
    obj.led1_state = GPIO.HIGH
    GPIO.output(LED1, obj.led1_state)

def set_mode2(obj : App):
    obj.state = State.MODE2 
    obj.rele_state = GPIO.HIGH 
    obj.led2_state = GPIO.HIGH
    GPIO.OUT(LED2, obj.led2_state) 
    obj.mode2_start_time = time.time() 

def set_mode3(obj : App):
    obj.state = State.MODE3 
    obj.rele_state = GPIO.HIGH
    obj.led1_state = GPIO.HIGH 
    obj.led3_state = GPIO.HIGH
    GPIO.OUT(LED1, obj.led1_state) 
    GPIO.OUT(LED3, obj.led3_state) 
   
def set_releoff(obj : App):
    obj.state = State.RELEOFF 
    obj.rele_state = GPIO.LOW 
    obj.led3_state = GPIO.HIGH
    GPIO.OUT(LED3, obj.led3_state) 

def turnoff_mode1(obj : App):
    obj.led1_state = GPIO.LOW 
    GPIO.OUT(LED1, obj.led1_state) 

def turnoff_mode2(obj : App):
    obj.led2_state = GPIO.LOW 
    GPIO.OUT(LED2, obj.led2_state) 

def turnoff_mode3(obj : App):
    obj.led1_state = GPIO.LOW
    obj.led3_state = GPIO.LOW 
    GPIO.OUT(LED1, obj.led1_state) 
    GPIO.OUT(LED3, obj.led3_state) 

def turnoff_releoff(obj : App):
    obj.led3_state = GPIO.LOW
    GPIO.OUT(LED3, obj.led3_state)
    

def blink_1_3(obj : App):
    obj.led1_state = ~obj.led1_state
    obj.led3_state = ~obj.led3_state
    GPIO.OUT(LED1, obj.led1_state)
    GPIO.OUT(LED3, obj.led3_state)    

