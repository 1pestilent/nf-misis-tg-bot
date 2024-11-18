from aiogram import Bot, Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

import re

from app.handlers.start import start_keyboard as kb
from app.handlers.start.start_state import RegisterState
from app.handlers.main import main_keyboard

from app.database.requests import DataBase

from app.core.dictionary import *
from app.core import valid



start_router = Router()

@start_router.message(Command(commands = 'start'))
async def hello_windows(message: Message, bot: Bot):
    db = DataBase()
    if not await db.get_user(message.from_user.id):
        await bot.send_message(message.from_user.id, text = register_message, reply_markup=await kb.register_kb())
    else:
        await bot.send_message(message.from_user.id, start_message)

@start_router.callback_query(F.data.startswith('register'))
async def start_register(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await bot.edit_message_reply_markup(chat_id=callback.from_user.id, message_id=callback.message.message_id, reply_markup=None)
    await callback.message.answer(indicate_email)
    await state.set_state(RegisterState.email)

@start_router.message(RegisterState.email)
async def register_email(message: Message, state: FSMContext, bot: Bot):
    if re.match(valid.email_validation, message.text):
        await state.update_data(email=message.text)
        await bot.send_message(message.from_user.id, choose_group, reply_markup = kb.groups_keyboard())
        await state.set_state(RegisterState.group)
    else:
        await bot.send_message(message.from_user.id, error_email)   
    

@start_router.message(RegisterState.group)
async def register_group(message: Message, state: FSMContext, bot: Bot):
    if message.text in current_groups:
        await state.update_data(group=message.text)
        dates = await state.get_data()

        db = DataBase()
        group_id = await db.get_group_id(dates['group'])
        user_id = message.from_user.id
        await db.add_user(user_id, message.from_user.username,dates["email"])
        await db.create_group_link(user_id, group_id)
        await bot.send_message(message.from_user.id, text = successful_registration, reply_markup = main_keyboard.main())
        await state.clear()
    else:
        await bot.send_message(message.from_user.id, error_group)