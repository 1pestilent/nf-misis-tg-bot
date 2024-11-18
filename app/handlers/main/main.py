from aiogram import Bot, Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from app.database.requests import DataBase
from app.handlers.main.main_keyboard import *
from app.handlers.main.main_state import EditEmailState, EditGroupState
from app.handlers.start.start_keyboard import groups_keyboard
from app.core.dictionary import *

import re
from app.core import valid

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

@main_router.callback_query(F.data.startswith('edit_email_call'))
async def start_edit_email(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await bot.send_message(callback.from_user.id, indicate_email)
    await state.set_state(EditEmailState.email)

@main_router.message(EditEmailState.email)
async def edit_email(message: Message, state: FSMContext, bot: Bot):
    if re.match(valid.email_validation, message.text):
        await state.update_data(email=message.text)
        data = await state.get_data()
        db = DataBase()
        if await db.update_user_email(message.from_user.id, data['email']):
            await  bot.send_message(message.from_user.id, succesesful_edit_email)
        else:
            await bot.send_message(message.from_user.id, fail_edit_email)
    else:
        await bot.send_message(message.from_user.id, error_email)   