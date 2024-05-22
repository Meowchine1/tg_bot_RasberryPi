from wiringPi.state import *

class App:
    led1_state = 1
    led2_state = 0
    led3_state = 0
    rele_state = 0
    mode2_start_time = 0
    previousMillis = 0
    state = State.MODE1