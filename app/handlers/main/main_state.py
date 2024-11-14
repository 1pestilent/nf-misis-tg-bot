from aiogram.fsm.state import StatesGroup, State

class EditEmailState(StatesGroup):
    email = State()

class EditGroupState(StatesGroup):
    group = State()

