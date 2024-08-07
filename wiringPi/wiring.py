#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import multiprocessing as mp
from wiringPi.gpio_management import *
from fs_out.write import write_log

try:
    set_mode1()
    while True:
        sygnal_val = GPIO.input(SYGNAL)
        app_state = get_state()
        if app_state == State.MODE1:
            if sygnal_val:
                set_rele_state(1)
            else:    
                turnoff_mode1()
                set_releoff()
                mess = "Произошло прерывание сигнала. Реле отключено!"
                push_message(mess)
        elif app_state == State.MODE2:
            current_time = current_milli_time()
            if get_mode2_start_time() < current_time - MODE2_INTERVAL:
                turnoff_mode2()
                set_mode1()
                mess = "Время второго режима истекло. Первый режим включен"
                push_message("Время второго режима истекло. Первый режим включен.")
                
        elif app_state == State.MODE3:
            currentMillis = current_milli_time()
            if currentMillis - get_previousMillis() >= BLINK_INTERVAL:
                blink_1_3()
                set_previousMillis(currentMillis)     
        

        GPIO.output(RELE, get_rele_state())
except KeyboardInterrupt:
    mess = "KeyboardInterrupt"
    print(mess)
    write_log(".", mess)
    GPIO.cleanup()
    sys.exit()
     


    

