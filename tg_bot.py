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
from wiring import app

mode1 = "Включить прерывание"
mode2 = "Отключить прерывание временно"
mode3 = "Отключить прерывание"
mode4 = "Посмотреть историю"
CHAT_ID  = 0
# Bot token can be obtained via https://t.me/BotFather
TOKEN = API_TOKEN

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
    global CHAT_ID
    CHAT_ID = message.chat.id
     
    await message.answer(f'Привет, {html.bold(message.from_user.full_name)})), '
                         'хочешь поуправлять мной? Выбирай режим...', reply_markup=keyboard)


# @dp.message()
# async def echo_handler(message: Message) -> None:
#     """
#     Handler will forward receive a message back to the sender

#     By default, message handler will handle all message types (like a text, photo, sticker etc.)
#     """
#     try:
#         # Send a copy of the received message
#         await message.send_copy(chat_id=message.chat.id)
#     except TypeError:
#         # But not all the types is supported to be copied so need to handle it
#         await message.answer("Nice try!")

def sendMessage(message):
    global CHAT_ID
    bot.send_message(CHAT_ID, message)
 
@dp.message(F.text.lower() == "test")
async def any_message(message: Message):
    id = message.from_user.id
    await message.answer(
        "Hello, <b>world</b>!", 
        parse_mode=ParseMode.HTML
    )
    await bot.send_message(CHAT_ID, "time")
    
@dp.message(F.text.lower() == mode1)
async def any_message(message: Message):
    turnoff_mode2()
    turnoff_mode3()
    turnoff_releoff()
    set_mode1()
    await message.reply("Прерывания включены") 
    

@dp.message(F.text.lower() == mode2)
async def any_message(message: Message):
    turnoff_mode1()
    turnoff_mode3()
    turnoff_releoff()
    set_mode2()
    await message.reply("Прерывания отключены временно на", MINUTES, "минут") 
    
    
@dp.message(F.text.lower() == mode3)
async def any_message(message: Message):
    set_mode3()
    turnoff_mode2()
    turnoff_mode1()
    turnoff_releoff()
    await message.reply("Прерывания отключены")  


@dp.message(F.text.lower() == mode4)
async def any_message(message: Message):
    await message.reply("Сейчас пришлю файл") 
    
    

async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
     
    # стало (функцией-регистратором)
    #dp.message.register(any_message, F.text)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
    
    

    