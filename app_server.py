import socket
import pickle
from multiprocessing.connection import Listener
from wiringPi.app import *

app = App()

# Создаем Listener для прослушивания запросов
address = ('localhost', 9999)
listener = Listener(address)

print("Server is running...")

while True:
    client = listener.accept()
    data = client.recv()
    if data:
        command, new_data = pickle.loads(data)
        if command == 'add_data':
            app.previousMillis = new_data
            print("Added data:", new_data)
        elif command == 'get_data':
            client.send(pickle.dumps(app.previousMillis))
            
            # -------------- GET ---------------------
        elif command == "get_state":
            client.send(pickle.dumps(app.state))
            
        elif command == "get_led1_state":
            client.send(pickle.dumps(app.led1_state))
            
        elif command == "get_led2_state":
            client.send(pickle.dumps(app.led2_state))
            
        elif command == "get_led3_state":
            client.send(pickle.dumps(app.led3_state))
            
        elif command == "get_mode2_start_time":
            client.send(pickle.dumps(app.mode2_start_time))
            
        elif command == "get_previousMillis":
            client.send(pickle.dumps(app.previousMillis))
            
            # ---------------- SET ---------------------
        elif command == "set_state":
            app.state = new_data
            client.send(pickle.dumps(app.state))
            print("Added data:", new_data)
            
        elif command == "set_led1_state":
            app.led1_state = new_data
            client.send(pickle.dumps(app.led1_state))
            print("Added data:", new_data)
            
        elif command == "set_led2_state":
            app.led2_state = new_data
            client.send(pickle.dumps(app.led2_state))
            print("Added data:", new_data)
            
        elif command == "set_led3_state":
            app.led3_state = new_data
            client.send(pickle.dumps(app.led3_state))
            print("Added data:", new_data)
            
        elif command == "set_mode2_start_time":
            app.mode2_start_time = new_data
            client.send(pickle.dumps(app.mode2_start_time))
            print("Added data:", new_data)
            
        elif command == "set_previousMillis":
            app.previousMillis = new_data
            client.send(pickle.dumps(app.previousMillis))
            print("Added data:", new_data)

    client.close()