from aiogram.fsm.state import State, StatesGroup

class Adverts(StatesGroup):
    adverts = State()

class Channel(StatesGroup):
    add = State()
    rem = State()

class Toy(StatesGroup):
    grooms_name = State()
    brides_name = State()
    wedding_date = State()
    full_address = State()
    location = State()
    description = State()
    
