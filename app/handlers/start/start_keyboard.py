from aiogram.types import KeyboardButton, ReplyKeyboardMarkup,InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from app.core import dictionary

def register_kb():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='🚀 Зарегистрироваться!',callback_data='register')]
        ])
    return keyboard

def groups_keyboard():
    keyboard = ReplyKeyboardBuilder()
    for group in dictionary.current_groups:
        keyboard.add(KeyboardButton(text=group))
    return keyboard.adjust(4).as_markup()