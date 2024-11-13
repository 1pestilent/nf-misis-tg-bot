import asyncio
import logging
from aiogram import Bot, Dispatcher

from dotenv import load_dotenv
import os

from app.handlers.start.start import start_router
from app.database.requests import *

load_dotenv()
token = os.getenv('TOKEN')

async def main():
    bot = Bot(token=token)
    dp = Dispatcher()
    dp.include_router(start_router)
    await dp.start_polling(bot)


if __name__=='__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')