import asyncio
import logging
import sys
import multiprocessing as mp
from aiogram.types  import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from aiogram import Bot, Dispatcher, html, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from wiringPi.config import API_TOKEN
from aiogram import F
from aiogram.filters import Command
from wiringPi.gpio_management import *

mode1 = "Включить прерывание"
mode2 = "Отключить прерывание временно"
mode3 = "Отключить прерывание"
mode4 = "Посмотреть историю"
CHAT_ID  = 0
# Bot token can be obtained via https://t.me/BotFather
TOKEN = API_TOKEN

def refresh_chatid(message: Message):
    global CHAT_ID
    CHAT_ID = message.chat.id
    

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
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

async def sendMessage(message):
    global CHAT_ID
    bot.send_message(CHAT_ID, message)


# Функция для отправки сообщения через таймер
async def send_message_by_timer():
    while True:
        # Задержка перед отправкой сообщения (например, 10 секунд)
        await asyncio.sleep(10)

        # ID пользователя, которому нужно отправить сообщение
        global CHAT_ID
        if CHAT_ID != 0:
            # Текст сообщения
            message_text = 'Привет! Это сообщение отправлено по таймеру.'
            # Отправляем сообщение пользователю
            await sendMessage(message_text)
        
 
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
    await message.reply("Режим 1 включен. Реле отключится при пропаже сигнала") 
    

@dp.message(F.text == mode2)
async def any_message(message: Message):
    turnoff_mode1()
    turnoff_mode3()
    turnoff_releoff()
    set_mode2()
    print("mode2")
    refresh_chatid(message)
    text = f"Режим 2. Без прерываний на {MINUTES} {TIME_NAME}"
    await message.reply(text) 
    
    
    
@dp.message(F.text == mode3)
async def any_message(message: Message):
    set_mode3()
    turnoff_mode2()
    turnoff_mode1()
    turnoff_releoff()
    print("mode3")
    refresh_chatid(message)
    await message.reply("Режим 3. Без прерываний")  


@dp.message(F.text == mode4)
async def any_message(message: Message):
    print("mode4")
    refresh_chatid(message)
    await message.reply("Сейчас пришлю файл") 
    
    

async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
     
    # стало (функцией-регистратором)
    #dp.message.register(any_message, F.text)
    # And the run events dispatching
    asyncio.create_task(send_message_by_timer())
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
    
    

    