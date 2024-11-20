from aiogram.types import KeyboardButton, InlineKeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from app.core.dictionary import *

button_list = ['⚙️ Настройки', '❔ Помощь', '✉️ Включить рассылку по почте', '✉️ Выключить рассылку по почте']

def main():
    keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='🗓️ Расписание')],
        [KeyboardButton(text='⚙️ Настройки'), KeyboardButton(text='❔ Помощь')]
        ], resize_keyboard= True, input_field_placeholder="Выбери действие!")
    return keyboard

def schedule():
    keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="Расписание на завтра")],
        [KeyboardButton(text="Расписание на неделю")],
        [KeyboardButton(text="Вернуться назад")],
        ], resize_keyboard= True, input_field_placeholder="Выбери действие!")
    return keyboard

def for_help():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='🧑‍💻 Ссылка на GitHub',url=link_github)),
    keyboard.add(InlineKeyboardButton(text='Наше сообщество в VK', url=link_vkgroup))
    return keyboard.adjust(1).as_markup()

def for_settings_unconfirm():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text=edit_email,callback_data='edit_email_call')),
    keyboard.add(InlineKeyboardButton(text=confirm_email, callback_data='confirm_email_call')),
    keyboard.add(InlineKeyboardButton(text=edit_group, callback_data='edit_group_call'))
    return keyboard.adjust(1).as_markup()

def for_settings_confirm_subscribed():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text=edit_email,callback_data='edit_email_call')),
    keyboard.add(InlineKeyboardButton(text=unsubscribe_email,callback_data='unsubscribe_email_call')),
    keyboard.add(InlineKeyboardButton(text=edit_group, callback_data='edit_group_call'))
    return keyboard.adjust(1).as_markup()

def for_settings_confirm():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text=edit_email,callback_data='edit_email_call')),
    keyboard.add(InlineKeyboardButton(text=subcsribe_email,callback_data='subscribe_email_call')),
    keyboard.add(InlineKeyboardButton(text=edit_group, callback_data='edit_group_call'))
    return keyboard.adjust(1).as_markup()