import asyncio
import logging
import sys
import multiprocessing as mp
from aiogram.types  import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton , \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import Bot, Dispatcher, html, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from wiringPi.config import API_TOKEN
from aiogram import F
from aiogram.filters import Command
from wiringPi.gpio_management import *
from multiprocessing import Process
from datetime import datetime, timedelta
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from fs_out.write import write_log, get_log_names

CHAT_ID  = 0
TOKEN = API_TOKEN

def refresh_chatid(message: Message):
    global CHAT_ID
    CHAT_ID = message.chat.id
    
# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
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
        input_field_placeholder="Выберите режим", 
     )
    refresh_chatid(message)
     
    await message.answer(f'Привет, {html.bold(message.from_user.full_name)})), '
                         'хочешь поуправлять мной? Выбирай режим...', reply_markup=keyboard)


# Функция для отправки сообщения через таймер
async def send_message_by_timer():
    global CHAT_ID
    print(CHAT_ID)
     
    if CHAT_ID != 0:
        message = get_message()
        if message:
            await bot.send_message(CHAT_ID, message)
 
@dp.message(F.text == "test")
async def any_message(message: Message):
    id = message.from_user.id
    refresh_chatid(message)
    await message.answer(
        "Hello, <b>world</b>!", 
        parse_mode=ParseMode.HTML
    )
    await bot.send_message(CHAT_ID, "time")
    
@dp.message(F.text == mode1)
async def any_message(message: Message):
    turnoff_mode2()
    turnoff_mode3()
    turnoff_releoff()
    set_mode1()
    print("mode1")
    refresh_chatid(message)
    log = "Режим 1 включен. Реле отключится при пропаже сигнала"
    write_log(".", log) 
    await message.reply(log)
     
    

@dp.message(F.text == mode2)
async def any_message(message: Message):
    turnoff_mode1()
    turnoff_mode3()
    turnoff_releoff()
    set_mode2()
    print("mode2")
    refresh_chatid(message)
    log = f"Режим 2. Без прерываний на {TIME_MEASURE} {TIME_NAME}"
    write_log(".", log) 
    await message.reply(log) 
    
    
    
@dp.message(F.text == mode3)
async def any_message(message: Message):
    set_mode3()
    turnoff_mode2()
    turnoff_mode1()
    turnoff_releoff()
    print("mode3")
    refresh_chatid(message)
    log = "Режим 3. Без прерываний"
    write_log(".", log)
    await message.reply(log)  


@dp.message(F.text == mode4)
async def any_message(message: Message):
    print("mode4")
    refresh_chatid(message)
    files = get_log_names(".")
    
    builder = InlineKeyboardBuilder()

    for file in files:
        builder.add(types.InlineKeyboardButton(
            text=file,
            callback_data=f"log_{file}")
        )   
    await message.answer("Выберите дату", reply_markup=builder.as_markup())     

@dp.callback_query(F.data.startswith("log_"))
async def callbacks_num(callback: types.CallbackQuery):
    log_file_name = callback.data.split("_")[1]
    if not is_file_exist(".", log_file_name):
        print("system error")
    else:
        print("file exist")    
    

    await callback.answer()

    #await message.reply("Выберите дату") 
    # keyboard = types.InlineKeyboardMarkup()
    # for file in files:
    #     keyboard.add(types.InlineKeyboardButton(text=file, callback_data=f"file_{file}"))
    # await message.reply("Выберите дату", reply_markup=keyboard)
    




async def main() -> None:

    scheduler = AsyncIOScheduler()
    scheduler.add_job(send_message_by_timer, trigger='interval', seconds=2, start_date=datetime.now())
    scheduler.start()
    await dp.start_polling(bot)



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
    
    

    