#!/usr/bin/python3

for txt_file in pathlib.Path('../logs').glob('*.txt'):
    ptint(txt_file)


from datetime import date


def check_logfile(date):
    for txt_file in pathlib.Path('../logs').glob('*.txt'):
        ptint(txt_file)
        # do something with "txt_file"

def write_log(message):
    today = date.today()

