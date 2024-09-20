from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
import logging

logging.basicConfig(level=logging.INFO)

API_TOKEN = '7818534299:AAFcQcJN4xMaOKq6kSJSIQjAQDN7AMK8F2o'

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("/start")

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
