from aiogram import Router, F 
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.handlers.start import start_keyboard as kb

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Привет, {message.from_user.username}. Ты зачислен(a) в ряды наших слонов! 🇷🇺', reply_markup=kb.main)



@router.message(F.text == "🗓️ Расписание")
async def schedule(message: Message):
    await message.answer(f'Выбери дату',reply_markup=kb.schedule)

@router.message(F.text == "Вернуться назад")
async def back(message: Message):
    await message.answer(f'Выбери действие', reply_markup=kb.main)