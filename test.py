import pickle
from multiprocessing.connection import Client
from wiringPi.gpio_management import State
def send_command(command, data=None):
    address = ('localhost', 9999)
    client = Client(address)
    client.send(pickle.dumps((command, data)))
    client.close()

def send_command2(command, data=None):
    address = ('localhost', 9999)
    client = Client(address)
    client.send(pickle.dumps((command, data)))
    response = client.recv()
    client.close()
    return pickle.loads(response)

def get_state():
    return send_command2('get_state')
def set_state(state: State):
    return send_command('set_state', state)


set_state(State.MODE2)
actual_state = get_state()

print(actual_state)
# # Пример использования
# #send_command('add_data', 4)
# data = send_command2('get_state')
# print("State:", data)
# if data == State.MODE1:
#     print("mode1")