from aiogram import Bot, Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from app.handlers.start import start_keyboard as kb
from app.handlers.start.start_state import RegisterState
from app.database.requests import DataBase
from app.core.dictionary import *

start_router = Router()

@start_router.message(Command(commands = 'start'))
async def hello_windows(message: Message, bot: Bot):
    db = DataBase()
    if not await db.get_user(message.from_user.id):
        await bot.send_message(message.from_user.id, f'{register_message}\n{message.from_user.id}', reply_markup=await kb.register_kb())
    else:
        await bot.send_message(message.from_user.id, start_message)

@start_router.callback_query(F.data.startswith('register'))
async def start_register(call: CallbackQuery, state: FSMContext):
    await call.message.answer('Укажите Ваш E-mail адрес')
    await state.set_state(RegisterState.email)
    await call.answer()

@start_router.message(RegisterState.email)
async def group_input(message: Message, state: FSMContext, bot: Bot):
    await bot.send_message(message.from_user.id, 'Выберите Вашу группу', reply_markup = kb.groups_keyboard())
    await state.update_data(name=message.text)
    await state.set_state(RegisterState.group)

@start_router.message(RegisterState.group)
async def correct_group_input(message: Message, state: FSMContext, bot: Bot):
    await state.update_data(group=message.text)
    user_data = await state.get_data()
    await bot.send_message(message.from_user.id, f'Твоя группа {user_data["group"]}')

    #await call.message.answer('Какая у тебя группа?', reply_markup=await kb.groups_keyboard())
    #group = state.get_data().get('user_input')  
    #await call.message.answer(f'Ты выбрал {group}')