from aiogram.types import KeyboardButton, ReplyKeyboardMarkup,InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from app.core import dictionary

async def register_kb():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='🚀 Зарегистрироваться!',callback_data='register')]
        ])
    return keyboard

def groups_keyboard():
    keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="БТМО"), KeyboardButton(text="БПИ"), KeyboardButton(text="БХТ")],
        [KeyboardButton(text="БЭК"), KeyboardButton(text="БМТ"), KeyboardButton(text="БЭЭ")],
    ], resize_keyboard= True, input_field_placeholder="Выберите действие!")
    return keyboard

async def groups_BTMO():
    keyboard = ReplyKeyboardBuilderkeyboard()
    for group in dictionary.group_BTMO:
        keyboard.add(KeyboardButton(text=group))
    return keyboard.adjust(2).as_markup()

async def groups_BPI():
    keyboard = ReplyKeyboardBuilderkeyboard()
    for group in dictionary.group_BPI:
        keyboard.add(KeyboardButton(text=group))
    return keyboard.adjust(2).as_markup()

async def groups_BHT():
    keyboard = ReplyKeyboardBuilderkeyboard()
    for group in dictionary.group_BHT:
        keyboard.add(KeyboardButton(text=group))
    return keyboard.adjust(2).as_markup()

async def groups_BEK():
    keyboard = ReplyKeyboardBuilderkeyboard()
    for group in dictionary.group_BEK:
        keyboard.add(KeyboardButton(text=group))
    return keyboard.adjust(2).as_markup()

async def groups_BMT():
    keyboard = ReplyKeyboardBuilderkeyboard()
    for group in dictionary.group_BMT:
        keyboard.add(KeyboardButton(text=group))
    return keyboard.adjust(2).as_markup()

async def groups_BEE():
    keyboard = ReplyKeyboardBuilderkeyboard()
    for group in dictionary.group_BEE:
        keyboard.add(KeyboardButton(text=group))
    return keyboard.adjust(2).as_markup()