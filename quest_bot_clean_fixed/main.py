
import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Привет! Это текстовый квест-бот. Введи /журнал чтобы посмотреть улику.")

@dp.message_handler(commands=["журнал"])
async def journal(message: types.Message):
    await message.answer("🔎 Ваша улика: обрывок письма с отпечатками...")

if __name__ == "__main__":
    executor.start_polling(dp)
