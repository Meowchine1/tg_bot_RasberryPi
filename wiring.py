#!/usr/bin/env python
# -*- coding: utf-8 -*-

import multiprocessing as mp
from wiringPi.gpio_management import *
from Telegram.tg import *

 

try:
    while True:
        sygnal_val = input(SYGNAL)

        if app.state == State.MODE1:
            if sygnal_val:
                app.rele_state = 1
            else:    
                turnoff_mode1(app)
                set_releoff(app)
        elif app.state == State.MODE2:
            current_time = time.time(app) 
            if app.mode2_start_time < current_time - MODE2_INTERVAL:
                turnoff_mode2(app)
                set_mode1(app)

        elif app.state == State.MODE3:
            currentMillis = time.time(app) 
            if currentMillis - app.previousMillis >= BLINK_INTERVAL:
                blink_1_3(app)
                app.previousMillis = currentMillis
        
        elif app.state == State.RELEOFF:
            sendMessage("Прерывание включено")
            # send to tg bot one message

        GPIO.output(RELE, app.rele_state)
except KeyboardInterrupt:
    print('interrupted!')


    


