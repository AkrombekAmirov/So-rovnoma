from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from file_service.file_write import read_student, read_group_
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from utils.db_api.db_core import *
from data.config import ADMINS
from keyboards.inline import *
from aiogram import types
from loader import dp
from states import *


@dp.message_handler(commands=['configuration'])
async def func(message: types.Message):
    if str(message.from_user.id) == str(ADMINS):
        await message.answer(text="Xizmat turini tanlang!", reply_markup=configuration)
    else:
        await message.answer("Siz bu foydalanuvchi emas!")


@dp.callback_query_handler(text="1", state="*")
async def one(call: CallbackQuery, state: FSMContext):
    await state.update_data({"one": call.data})
    await call.message.answer(text="Guruhni nomini kiriting! Hemis platformasi buyicha kiriting!")
    await Configuration.one.set()


@dp.message_handler(state=Configuration.one)
async def two(message: types.Message, state: FSMContext):
    if await read_group_(message.text) is None:
        await message.answer(text="Guruh topilmadi. Iltimos qaytadan urunib ko'ring!")
        await Configuration.one.set()
    elif await read_group_(message.text):
        await state.update_data({"two": message.text})
        if read_group(str(message.text)):
            await message.answer(text="Bu guruh avval nyaratilgan,Iltimos qaytadan urinib kuring",
                                 reply_markup=configuration)
        elif read_group(str(message.text)) is None:
            create_group(group=message.text, teacher_id=None, teacher_name=None)
            await message.answer(text="Guruh muvaffaqiyatli yaratildi!", reply_markup=configuration)


@dp.callback_query_handler(text="2", state="*")
async def three(call: CallbackQuery, state: FSMContext):
    inline_keyboard = InlineKeyboardMarkup(row_width=1)

    for group in read_all_groups():
        button = InlineKeyboardButton(text=group.group, callback_data=f"group_{group.group}")
        inline_keyboard.insert(button)
    await call.message.answer(text="Guruhlar haqida malumot", reply_markup=inline_keyboard)


@dp.callback_query_handler(lambda call: call.data.startswith("group_"), state="*")
async def three(call: CallbackQuery, state: FSMContext):
    await state.update_data({"group": call.data})
    print(call.data)
    await call.message.answer(text="Xizmat turini tanlang!", reply_markup=teacher)


@dp.callback_query_handler(lambda call: call.data.startswith("teacher_"), state="*")
async def three(call: CallbackQuery, state: FSMContext):
    await call.message.answer("asdnskajndkjsa", reply_markup=teacher)
