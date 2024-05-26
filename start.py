import os
import signal
import subprocess
import RPi.GPIO as GPIO

# Запуск всех приложений
subprocess.Popen(['python', './app_server.py'])
subprocess.Popen(['python', './tg_bot.py'])
subprocess.Popen(['python', './wiring.py'])

try:
    while True:
        pass
except KeyboardInterrupt:
    # Остановка всех процессов Python
    GPIO.cleanup()
    os.system("pkill -f 'python ./app_server.py'")
    os.system("pkill -f 'python ./tg_bot.py'")
    os.system("pkill -f 'python ./wiring.py'")