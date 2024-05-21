
 

from wiringPi.gpio_management import *
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from aiogram import F
from aiogram.filters.command import Command

from wiringPi.config import API_TOKEN
# from telegram_menu import BaseMessage, TelegramMenuSession, NavigationHandler

CHAT_ID  = ""
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

mode1 = "Включить прерывание"
mode2 = "Отключить прерывание временно"
mode3 = "Отключить прерывание"
mode4 = "Посмотреть историю"

def sendMessage(message):
    bot.send_message(CHAT_ID, message)

@dp.message(Command("start"))
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
   CHAT_ID = message.chat.id
   await message.reply(reply_markup=keyboard)

@dp.message(F.text.lower() == mode1)
async def choose_mode1(message: types.Message):
    turnoff_mode2()
    turnoff_mode3()
    turnoff_releoff()
    set_mode1()
    await message.reply("Прерывания включены") 

@dp.message(F.text.lower() == mode2)
async def choose_mode2(message: types.Message):
    turnoff_mode1()
    turnoff_mode3()
    turnoff_releoff()
    set_mode2()
    await message.reply("Прерывания отключены временно на", MINUTES, "минут") 
   
@dp.message(F.text.lower() == mode3)
async def choose_mode3(message: types.Message):
    set_mode3()
    turnoff_mode2()
    turnoff_mode1()
    turnoff_releoff()
    await message.reply("Прерывания отключены") 

@dp.message(F.text.lower() == mode4)
async def get_inf(message: types.Message):
    await message.reply("Сейчас пришлю файл") 
    turnoff_mode1()
    turnoff_mode2()
    turnoff_mode3()
    set_releoff()

dp.start_polling(bot)
# executor.start_polling(dp, skip_updates=True)