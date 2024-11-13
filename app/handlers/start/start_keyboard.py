from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='🗓️ Расписание')],
    [KeyboardButton(text='⚙️ Настройки'), KeyboardButton(text='❔ Помощь')]
], resize_keyboard= True, input_field_placeholder="Выберите действие!")

schedule = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Расписание на завтра")],
    [KeyboardButton(text="Расписание на неделю")],
    [KeyboardButton(text="Вернуться назад")],
], resize_keyboard= True, input_field_placeholder="Выберите действие!")