##!/usr/bin/python3

from datetime import date, datetime
import os 
from os import listdir, path
from os.path import isfile, join
 
def write_log(relative_path, message):
    log_data = f'[{datetime.now().time()} -- {message}]'
    buffer = '' 
    day_log = f"{relative_path}/logs/{date.today()}.txt"


    if not os.path.exists(day_log):
        with open(day_log, 'w') as file:
            file.write(log_data) 
    else:
        with open(day_log, 'r') as file:
            for line in file:
                buffer += line
            buffer += '\n' + log_data  
        with open(day_log, 'w') as file:
            file.write(buffer)

 
 
def is_file_exist(relative_path, filename):
    day_log = f"{relative_path}/logs/{filename}.txt"
    return os.path.exists(day_log)


def get_log_names(relative_path):
    names = [f for f in listdir(relative_path+"/logs/") if isfile(join(relative_path+"/logs/", f))]
    names_filtered = []
    for name in names:
        name, ext = path.splitext(name)
        names_filtered.append(name)

    return names


# print(is_file_exist("..", "2024-06-10"))
# print(get_log_names(".."))