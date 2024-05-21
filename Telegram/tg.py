
API_TOKEN = '6954679719:AAGiP1WfhiY8DV3ku-04w_eMwzlXs83SCZI'

from wiringPi.gpio_management import *
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from aiogram import F
from telegram_menu import BaseMessage, TelegramMenuSession, NavigationHandler

CHAT_ID  = ""
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

mode1 = "Включить прерывание"
mode2 = "Отключить прерывание временно"
mode3 = "Отключить прерывание"
mode4 = "Посмотреть историю"

def sendMessage(message):
    bot.send_message(CHAT_ID, message)

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
   CHAT_ID = message.chat.id
   await message.reply(reply_markup=keyboard)

@dp.message(F.text.lower() == mode1)
async def with_puree(message: types.Message):
    turnoff_mode2()
    turnoff_mode3()
    turnoff_releoff()
    set_mode1()
    await message.reply("Прерывания включены") 

@dp.message(F.text.lower() == mode2)
async def without_puree(message: types.Message):
    turnoff_mode1()
    turnoff_mode3()
    turnoff_releoff()
    set_mode2()
    await message.reply("Прерывания отключены временно на", MINUTES, "минут") 
   
@dp.message(F.text.lower() == mode3)
async def without_puree(message: types.Message):
    set_mode3()
    turnoff_mode2()
    turnoff_mode1()
    turnoff_releoff()
    await message.reply("Прерывания отключены") 

@dp.message(F.text.lower() == mode4)
async def without_puree(message: types.Message):
    await message.reply("Сейчас пришлю файл") 
    turnoff_mode1()
    turnoff_mode2()
    turnoff_mode3()
    set_releoff()

executor.start_polling(dp, skip_updates=True)