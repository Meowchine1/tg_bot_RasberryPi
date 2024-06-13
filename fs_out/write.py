#!/usr/bin/python3

from datetime import date, datetime
import os 
from os import listdir, path
from os.path import isfile, join
 
def write_log(relative_path, message):
    log_data = f'[{datetime.now().time()} | message: {message}]'
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
    day_log = f"{relative_path}/logs/{filename}"
    return os.path.exists(day_log)


def get_log_names(relative_path, count=0):

    names = [(f, datetime.fromtimestamp(os.path.getctime(join(relative_path+"/logs/", f)))) \
    for f in listdir(relative_path+"/logs/") if isfile(join(relative_path+"/logs/", f)) and f.endswith('.txt')]
 
    names.sort(key=lambda x: x[1])
     
    if count > 0:
        if count < len(names):
            names = names[-1:count*(-1)-1:-1]
    #print(names)
    names_filtered = []
    for name, date in names:
        name, ext = path.splitext(name)
        names_filtered.append(name)
     
    return names_filtered


def get_months(relative_path):
    months = []
    dirr = os.listdir(relative_path+"/logs/")
    for filename in dirr:
        if filename.endswith('.txt') and len(filename) == 14 and filename.count('-') == 2:
            try:
                filename = filename.split(".")[0]
                date = datetime.strptime(filename, '%Y-%m-%d').date()
                if date.month not in months:
                    months.append(date.month)
            except ValueError:
                pass
    return months

def get_days(relative_path):
    days = []
    dirr = os.listdir(relative_path+"/logs/")
    for filename in dirr:
        if filename.endswith('.txt') and len(filename) == 14 and filename.count('-') == 2:
            try:
                filename = filename.split(".")[0]
                date = datetime.strptime(filename, '%Y-%m-%d').date()
                if date.day not in days:
                    days.append(date.day)
            except ValueError:
                pass
    return days

def get_file_name(mounth, day):
    if day / 10 == 0:
        filename = str(datetime.now().year) + "-0" + str(mounth) + "-" + str(day) + ".txt"
    else:
        filename = str(datetime.now().year) + "-0" + str(mounth) + "-" + str(day) + ".txt"    
    print(filename)



#get_file_name(6, 10)
#print(get_days(".."))
#print(get_mounths(".."))

print(get_log_names("..", 7))

# print(is_file_exist("..", "2024-06-10"))
# print(get_log_names(".."))