from app_api import  get_state
from wiringPi.state import *
from fs_out.write import write_log


app_state = get_state()
while(1):
    print("APP STATE IS ", app_state)
    actual_app_state = get_state()

    if actual_app_state != app_state:

        log = f" Переход из состояния {states_text[app_state.value]} --> {states_text[actual_app_state.value]}"
        write_log(".", log)
        app_state = actual_app_state

