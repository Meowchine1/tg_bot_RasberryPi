#!/usr/bin/python3

import os 
from os import listdir, path
from os.path import isfile, join

def write_log():
    log_data = "test"
    for i in range(1, 30):
        day_log = f"./2024-05-{i}.txt"
        if not os.path.exists(day_log):
            with open(day_log, 'w') as file:
                file.write(log_data)


write_log()