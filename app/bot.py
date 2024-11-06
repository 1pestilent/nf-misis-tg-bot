import asyncio
import logging
from aiogram import Bot, Dispatcher

from dotenv import load_dotenv
import os

from app.handlers.user import router

load_dotenv()
token = os.getenv('TOKEN')

bot = Bot(token=token)
dp = Dispatcher()

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__=='__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')