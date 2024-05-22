#!/usr/bin/env python
# -*- coding: utf-8 -*-

import multiprocessing as mp
from wiringPi.gpio_management import *
from tg_bot import *


try:
    while True:
        sygnal_val = GPIO.input(SYGNAL)
        app_state = get_state()

        if app_state == State.MODE1:
            if sygnal_val:
                set_rele_state(1)
            else:    
                turnoff_mode1()
                set_releoff()
        elif app_state == State.MODE2:
            current_time = time.time() 
            if get_mode2_start_time() < current_time - MODE2_INTERVAL:
                turnoff_mode2()
                set_mode1()

        elif app_state == State.MODE3:
            currentMillis = time.time() 
            if currentMillis - get_previousMillis() >= BLINK_INTERVAL:
                blink_1_3()
                set_previousMillis(currentMillis)
        
        elif app_state == State.RELEOFF:
            sendMessage("Произошло прерывание. Реле отключено!")
            # send to tg bot one message

        GPIO.output(RELE, get_rele_state())
except KeyboardInterrupt:
    print('interrupted!')


    


