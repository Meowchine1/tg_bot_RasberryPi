#!/usr/bin/env python
# -*- coding: utf-8 -*-


import wiringPi.gpio_management
import Telegram.tg

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from aiogram import F
from telegram_menu import BaseMessage, TelegramMenuSession, NavigationHandler


# Делаем сброс состояний портов (все конфигурируются на вход - INPUT)
GPIO.cleanup()
# Режим нумерации пинов - по названию (не по порядковому номеру на разъеме)
GPIO.setmode(GPIO.BCM)


GPIO.setup(SYGNAL, GPIO.IN)
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)
GPIO.setup(RELE, GPIO.OUT)

GPIO.output(LED1, GPIO.LOW)
GPIO.output(LED2, GPIO.LOW)
GPIO.output(LED3, GPIO.LOW)
GPIO.output(RELE, GPIO.LOW)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

mode1 = "Включить прерывание"
mode2 = "Отключить прерывание временно)"
mode3 = "Отключить прерывание отключено)"
mode4 = "Посмотреть историю"


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
   kb = [
       [
           types.KeyboardButton(text=mode1),
           types.KeyboardButton(text=mode2),
           types.KeyboardButton(text=mode3),
           types.KeyboardButton(text=mode4)
       ],
   ]
   keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите режим"
    )
   await message.reply(reply_markup=keyboard)



@dp.message(F.text.lower() == mode1)
async def with_puree(message: types.Message):
    set_mode1()
    turnoff_mode2()
    turnoff_mode3()
    turnoff_releoff()

@dp.message(F.text.lower() == mode2)
async def without_puree(message: types.Message):
    set_mode2()
    turnoff_mode1()
    turnoff_mode3()
    turnoff_releoff()
   
@dp.message(F.text.lower() == mode3)
async def without_puree(message: types.Message):
    set_mode3()
    turnoff_mode2()
    turnoff_mode1()
    turnoff_releoff()

@dp.message(F.text.lower() == mode4)
async def without_puree(message: types.Message):
    await message.reply("Так невкусно!") 
    

sygnal_val = input(SYGNAL)

if state == State.MODE1:
    digitalWrite(LED1, led1_state)
    if sygnal_val:
        rele_state = 1
    else:    
        turnoff_mode1()
        set_releoff()
elif state == State.MODE2:
    current_time = time.time() 
    if mode2_start_time < current_time - MODE2_INTERVAL:
        turnoff_mode2()
        set_mode1()

elif state == State.MODE3:
    currentMillis = time.time() 
    if currentMillis - previousMillis >= BLINK_INTERVAL:
        led1_state = ~led1_state
        led3_state = ~led3_state
        digitalWrite(LED1, led1_state)
        digitalWrite(LED3, led3_state)
        previousMillis = currentMillis
        
elif state == State.RELEOFF:
    # send to tg bot one message


GPIO.output(RELE, rele_state)
    

   
if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)   
      

