from aiogram import Bot, Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from app.database.requests import DataBase
from app.handlers.main.main_keyboard import *
from app.core.dictionary import *


main_router = Router()

@main_router.message(Command('help'))
async def get_help(message: Message):
    await message.answer(help_message, reply_markup=for_help())

@main_router.message(Command('settings'))
async def get_settings(message:Message):
    db = DataBase()
    user_email = await db.get_user_email(message.from_user.id)
    user_group = await db.get_group_names_by_user_id(message.from_user.id)
    await message.answer(f'Твоя почта: {user_email}\nТвоя группа: {user_group}',reply_markup=for_settings_unconfirm())


@main_router.message(lambda message: message.text in button_list)
async def text_handler(message: Message):
    if message.text == button_list[0]:
        await get_settings(message)
    elif message.text == button_list[1]:
        await get_help(message)