import socket
import pickle
from multiprocessing.connection import Listener
from wiringPi.app import *

app = App()
#get_rele_state
#set_rele_state
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

        elif command == 'get_data':
            client.send(pickle.dumps(app.previousMillis))
            
            # -------------- GET ---------------------
        elif command == "get_state":
            client.send(pickle.dumps(app.state))

        elif command == "get_rele_state":
            client.send(pickle.dumps(app.rele_state))
            
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
        elif command == "get_message":
            if app.message_q.empty():
                client.send(pickle.dumps(0))
            else:     
                client.send(pickle.dumps(app.message_q.get()))   
            
            # ---------------- SET ---------------------
        elif command == "set_state":
            app.state = new_data
            client.send(pickle.dumps(app.state))

        elif command == "set_rele_state":
            app.rele_state = new_data
            client.send(pickle.dumps(app.rele_state))
            
        elif command == "set_led1_state":
            app.led1_state = new_data
            client.send(pickle.dumps(app.led1_state))
            
        elif command == "set_led2_state":
            app.led2_state = new_data
            client.send(pickle.dumps(app.led2_state))
            
        elif command == "set_led3_state":
            app.led3_state = new_data
            client.send(pickle.dumps(app.led3_state))
            
        elif command == "set_mode2_start_time":
            app.mode2_start_time = new_data
            client.send(pickle.dumps(app.mode2_start_time))
            
        elif command == "set_previousMillis":
            app.previousMillis = new_data
            client.send(pickle.dumps(app.previousMillis))

        elif command == "push_message":
            app.message_q.put(new_data)
            client.send(pickle.dumps(1))
        else:
            print("Wrong api command")    

    client.close()