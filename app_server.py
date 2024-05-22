import socket
import pickle
from multiprocessing.connection import Listener
from wiringPi.gpio_management import App 

app = App()

# Создаем Listener для прослушивания запросов
address = ('localhost', 9999)
listener = Listener(address)

print("Server is running...")



#   led1_state = GPIO.HIGH
#     led2_state = GPIO.LOW
#     led3_state = GPIO.LOW
#     rele_state = GPIO.LOW
#     mode2_start_time = 0
#     previousMillis = 0
#     state = State.MODE1

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
            
        elif command == "set_state":
            app.state = new_data
            print("Added data:", new_data)
            
        elif command == "set_led1_state":
            app.led1_state = new_data
            print("Added data:", new_data)
            
        elif command == "set_led2_state":
            app.led2_state = new_data
            print("Added data:", new_data)
            
        elif command == "set_led3_state":
            app.led3_state = new_data
            print("Added data:", new_data)
            
        elif command == "set_mode2_start_time":
            app.mode2_start_time = new_data
            print("Added data:", new_data)
            
        elif command == "set_previousMillis":
            app.previousMillis = new_data
            print("Added data:", new_data)

    client.close()