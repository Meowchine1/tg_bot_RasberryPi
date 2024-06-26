#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import multiprocessing as mp
from wiringPi.gpio_management import *
from fs_out.write import write_log

try:
    #setup_pin()
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
                #print(mess)
                #write_log(".", mess)
        elif app_state == State.MODE2:
            current_time = current_milli_time()
            #print(f"current time = {current_time}, mode2_start = {get_mode2_start_time()} \n")
            if get_mode2_start_time() < current_time - MODE2_INTERVAL:
                turnoff_mode2()
                set_mode1()
                mess = "Время второго режима истекло. Первый режим включен"
                #print("Время второго режима истекло. Первый режим включен")
                push_message("Время второго режима истекло. Первый режим включен.")
                #write_log(".", mess)

        elif app_state == State.MODE3:
            currentMillis = current_milli_time()
            #print(f"current time = {currentMillis}, BLINK_INTERVAL = {BLINK_INTERVAL} \n")
            if currentMillis - get_previousMillis() >= BLINK_INTERVAL:
                blink_1_3()
                set_previousMillis(currentMillis)     
        
        #elif app_state == State.RELEOFF:

        GPIO.output(RELE, get_rele_state())
except KeyboardInterrupt:
    mess = "KeyboardInterrupt"
    print(mess)
    write_log(".", mess)
    GPIO.cleanup()
    sys.exit()
     


    

