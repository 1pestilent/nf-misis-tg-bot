from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def main():
    keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='🗓️ Расписание')],
        [KeyboardButton(text='⚙️ Настройки'), KeyboardButton(text='❔ Помощь')]
        ], resize_keyboard= True, input_field_placeholder="Выберите действие!")
    return keyboard

def schedule():
    keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="Расписание на завтра")],
        [KeyboardButton(text="Расписание на неделю")],
        [KeyboardButton(text="Вернуться назад")],
        ], resize_keyboard= True, input_field_placeholder="Выберите действие!")
    return keyboard

