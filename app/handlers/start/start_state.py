from aiogram.fsm.state import StatesGroup, State

class RegisterState(StatesGroup):
    email = State()
    group = State()
    