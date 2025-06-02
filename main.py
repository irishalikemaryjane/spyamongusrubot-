import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Привет! Это тестовое сообщение от квест-бота.")

@dp.message_handler(commands=["журнал"])
async def journal(message: types.Message):
    await message.answer("🔍 Ваша улика будет храниться здесь...")

if __name__ == "__main__":
    executor.start_polling(dp)
