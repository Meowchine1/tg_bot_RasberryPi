#!/usr/bin/env python
# -*- coding: utf-8 -*-


from wiringPi.gpio_management import *
from Telegram.tg import *

try:
    while True:
        sygnal_val = input(SYGNAL)

        if state == State.MODE1:
            GPIO.OUT(LED1, led1_state)
            if sygnal_val:
                rele_state = 1
            else:    
                turnoff_mode1()
                set_releoff()
        elif state == State.MODE2:
            current_time = time.time() 
            if mode2_start_time < current_time - MODE2_INTERVAL:
                turnoff_mode2()
                set_mode1()

        elif state == State.MODE3:
            currentMillis = time.time() 
            if currentMillis - previousMillis >= BLINK_INTERVAL:
                led1_state = ~led1_state
                led3_state = ~led3_state
                GPIO.OUT(LED1, led1_state)
                GPIO.OUT(LED3, led3_state)
                previousMillis = currentMillis
        
        elif state == State.RELEOFF:
            sendMessage("Прерывание включено")
            # send to tg bot one message


        GPIO.output(RELE, rele_state)
except KeyboardInterrupt:
    print('interrupted!')


    
  
      

