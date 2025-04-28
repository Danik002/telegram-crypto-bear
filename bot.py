from aiogram import Bot, Dispatcher, executor, types
import os

bot = Bot(token=os.getenv("8101281521:AAED2vrovopOil8FeAX4xHnuHpEvtyZHNhI"))  # Токен берется из переменных окружения
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привет! Я крипто-бот! 🐻")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
