from aiogram import Bot, Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from app.database.requests import DataBase
from app.handlers.main.main_keyboard import *
from app.handlers.main.main_state import EditEmailState, EditGroupState, ConfirmEmailState
from app.handlers.start.start_keyboard import groups_keyboard
from app.core.dictionary import *
from app.core.mailing import auth_mail
from app.core.key_generator import generate_key

import re
from app.core import valid

main_router = Router()

@main_router.message(Command('help'))
async def get_help(message: Message):
    await message.answer(help_message, reply_markup=for_help())

@main_router.message(Command('settings'))
async def get_settings(message: Message):
    db = DataBase()
    user_email = await db.get_user_email(message.from_user.id)
    user_group = await db.get_group_names_by_user_id(message.from_user.id)
    text = (f'Настройки:\n\nТвоя почта: {user_email}\nТвоя группа: {user_group}')
    if not await db.check_email_confirm(message.from_user.id):
        await message.answer(text, reply_markup=for_settings_unconfirm())    
    else:
        if not await db.check_email_subscribe(message.from_user.id):
            await message.answer(text, reply_markup=for_settings_confirm())
        else:  
            await message.answer(text, reply_markup=for_settings_confirm_subscribed())

@main_router.message(Command('subscribe'))
async def subscribe(message: Message):
    await message.answer(succesesful_subscribe, reply_markup=main())

@main_router.message(Command('unsubscribe'))
async def unsubscribe(message: Message):
    await message.answer(succesesful_unsubscribe, reply_markup=main())

@main_router.message(lambda message: message.text in button_list)
async def text_handler(message: Message):
    if message.text == button_list[0]:
        await get_settings(message)
    elif message.text == button_list[1]:
        await get_help(message)
    elif message.text == button_list[2]:
        await subscribe()
    elif message.text == button_list[3]:
        await unsubscribe()

@main_router.callback_query(F.data.startswith('edit_email_call'))
async def start_edit_email(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await bot.edit_message_reply_markup(chat_id=callback.from_user.id, message_id=callback.message.message_id, reply_markup=None)
    await bot.send_message(callback.from_user.id, indicate_email)
    await state.set_state(EditEmailState.email)

@main_router.message(EditEmailState.email)
async def edit_email(message: Message, state: FSMContext, bot: Bot):
    if re.match(valid.email_validation, message.text):
        await state.update_data(email=message.text)
        data = await state.get_data()
        db = DataBase()
        if await db.update_user_email(message.from_user.id, data['email']):
            await  bot.send_message(message.from_user.id, succesesful_edit_email, reply_markup=main())
        else:
            await bot.send_message(message.from_user.id, error_edit_email)
    else:
        await bot.send_message(message.from_user.id, error_email)   

@main_router.callback_query(F.data.startswith('edit_group_call'))
async def start_group_edit(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await bot.edit_message_reply_markup(chat_id=callback.from_user.id, message_id=callback.message.message_id, reply_markup=None)
    await bot.send_message(callback.from_user.id, choose_group, reply_markup=groups_keyboard())
    await state.set_state(EditGroupState.group)

@main_router.message(EditGroupState.group)
async def edit_group(message: Message, state: FSMContext, bot: Bot):
    if message.text in current_groups:
        await state.update_data(group=message.text)
        data = await state.get_data()

        db = DataBase()
        await db.update_user_group(message.from_user.id, data["group"])
        await bot.send_message(message.from_user.id, text = succesesful_edit_group, reply_markup=main())
        await state.clear()
    else:
        await bot.send_message(message.from_user.id, error_group)

@main_router.callback_query(F.data.startswith('confirm_email_call'))
async def start_confirm_email(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await bot.edit_message_reply_markup(chat_id=callback.from_user.id, message_id=callback.message.message_id, reply_markup=None)

    db = DataBase()
    email = await db.get_user_email(callback.from_user.id)
    code = generate_key()

    await auth_mail(email, code)

    await bot.send_message(callback.from_user.id, f'{confirm_code_email}\n Code: {code}')
    await state.update_data(code = code)
    await state.set_state(ConfirmEmailState.ccode)

@main_router.message(ConfirmEmailState.ccode)
async def edit_email(message: Message, state: FSMContext, bot: Bot):
    await state.update_data(ccode=message.text)
    data = await state.get_data()
    if data['code'] == data['ccode']:
        db = DataBase()
        await db.update_email_confirm(message.from_user.id)
        await bot.send_message(message.from_user.id, f'✅ Ваша почта подтверждена')
    else:
        await bot.send_message(message.from_user.id, f'Код подтверждения указан не верно. Попробуйте еще раз!', reply_markup=main())
        await state.clear()

@main_router.callback_query(F.data.startswith('subscribe_email_call'))
async def subscribe(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await bot.edit_message_reply_markup(chat_id=callback.from_user.id, message_id=callback.message.message_id, reply_markup=None)

    db = DataBase()
    await db.update_email_subscribe(callback.from_user.id)
    await bot.send_message(callback.from_user.id, text=succesesful_subscribe, reply_markup=main())

@main_router.callback_query(F.data.startswith('unsubscribe_email_call'))
async def unsubscribe(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await bot.edit_message_reply_markup(chat_id=callback.from_user.id, message_id=callback.message.message_id, reply_markup=None)

    db = DataBase()
    await db.update_email_subscribe(callback.from_user.id)
    await bot.send_message(callback.from_user.id, text=succesesful_unsubscribe, reply_markup=main())