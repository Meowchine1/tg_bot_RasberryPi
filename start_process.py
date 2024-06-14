#!/usr/bin/python3


import multiprocessing as mp
#import RPi.GPIO as GPIO

#from wiring import *
from tg_bot import *
from logger import *
from app_server import *


app_p = mp.Process(target=appServerLoop)
#wiring_p = mp.Process(target=wiring_loop)
tg_p = mp.Process(target=start_tg)
log_p = mp.Process(target=log_loop)


app_p.start()

# when app port bacomes availiable

#wiring_p.start()
tg_p.start()
log_p.start()


try:
    while True:
        pass
except KeyboardInterrupt:
    # Остановка всех процессов Python
    GPIO.cleanup()
    log_p.kill()
    tg_p.kill()
    #wiring_p.kill()
    app_p.kill()
    

