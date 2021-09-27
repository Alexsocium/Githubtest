from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message)
    await message.reply('Hello /start')
