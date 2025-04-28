import logging
from aiogram import Bot, Dispatcher, executor, types
import os

# Настройка логов
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    bot = Bot(token=os.getenv("BOT_TOKEN"))
    dp = Dispatcher(bot)
    
    @dp.message_handler(commands=['start'])
    async def start(message: types.Message):
        await message.answer("Бот работает! 🚀")
        logger.info(f"User {message.from_user.id} started bot")

    if __name__ == '__main__':
        logger.info("Starting bot...")
        executor.start_polling(dp, skip_updates=True)

except Exception as e:
    logger.error(f"Bot failed: {e}", exc_info=True)
    raise
