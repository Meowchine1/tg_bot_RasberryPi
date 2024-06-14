#!/usr/bin/python3

import os
import signal
import subprocess
import RPi.GPIO as GPIO
import time
import psutil


def is_port_occupied_by_process(port, process_name):
  """Проверяет, занят ли порт заданным процессом.

  Args:
    port: Номер порта.
    process_name: Имя процесса (например, "app_server.py").

  Returns:
    True, если порт занят процессом с заданным именем, False в противном случае.
  """
  for connection in psutil.net_connections():
    if connection.laddr.port == port:
      # Проверяем, является ли имя процесса совпадающим
      try:
        process = psutil.Process(connection.pid)
        print(process.name())
        if process_name in process.name():
          return True
      except (psutil.NoSuchProcess, psutil.AccessDenied):
        pass  # Процесс уже завершился или у нас нет прав на доступ
  return False

 
   

# Запуск всех приложений

subprocess.Popen(['python3', './app_server.py'])
time.sleep(3)
# port = 9999
# process_name = "python"

# if is_port_occupied_by_process(port, process_name):
#    print(f"Порт {port} занят процессом {process_name}")
# else:
#    print(f"Порт {port} не занят процессом {process_name}")


subprocess.Popen(['python', './tg_bot.py'])
subprocess.Popen(['python', './wiring.py'])
subprocess.Popen(['python', './logger.py'])

try:
    while True:
        pass
except KeyboardInterrupt:
    # Остановка всех процессов Python
    GPIO.cleanup()
    os.system("pkill -f 'python ./tg_bot.py'")
    os.system("pkill -f 'python ./wiring.py'")
    os.system("pkill -f 'python ./logger.py'")
    os.system("pkill -f 'python ./app_server.py'")