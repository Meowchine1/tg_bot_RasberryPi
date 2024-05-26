import pickle
from multiprocessing.connection import Client
from wiringPi.app import *

#   if no response
# def send_command(command, data=None):
#     address = ('localhost', 9999)
#     client = Client(address)
#     client.send(pickle.dumps((command, data)))
#     client.close()

def send_command(command, data=None):
    address = ('localhost', 9999)
    client = Client(address)
    client.send(pickle.dumps((command, data)))
    response = client.recv()
    client.close()
    return pickle.loads(response)


def get_state():
    return send_command('get_state')
def set_state(state: State):
    return send_command('set_state', state)

def get_led1_state():
    return send_command('get_led1_state')
def set_led1_state(state: int):
    return send_command('set_led1_state', state)

def get_led2_state():
    return send_command('get_led2_state')
def set_led2_state(state: int):
    return send_command('set_led2_state', state)

def get_led3_state():
    return send_command('get_led3_state')
def set_led3_state(state: int):
    return send_command('set_led3_state', state)

def get_rele_state():
    return send_command('get_rele_state')
def set_rele_state(state: int):
    return send_command('set_rele_state', state)

def get_mode2_start_time():
    return send_command('get_mode2_start_time')
def set_mode2_start_time(time: int):
    return send_command('set_mode2_start_time', time)

def get_previousMillis():
    return send_command('get_previousMillis')
def set_previousMillis(time: int):
    return send_command('set_previousMillis', time)

def get_message():
    return send_command('get_message')

def push_message(message: str):
    return send_command('push_message', message)
