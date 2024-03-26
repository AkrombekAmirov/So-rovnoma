from aiogram.dispatcher.filters.state import State, StatesGroup


class Question(StatesGroup):
    hemis_id = State()
    one = State()
    two = State()
    three = State()
    four = State()
    five = State()
    six = State()
    seven = State()
    eight = State()
    nine = State()
    ten = State()
    eleven = State()
    twelve = State()
    thirteen = State()


class Admin(StatesGroup):
    start = State()
    end = State()


class Configuration(StatesGroup):
    one = State()
    two = State()
    three = State()
    four = State()
    five = State()
    six = State()
    seven = State()
    eight = State()
    nine = State()
    ten = State()
    eleven = State()
    twelve = State()
    thirteen = State()


class ConfigurationTwo(StatesGroup):
    sex = State()
    seven = State()
