from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from file_service.file_write import read_student, read_group_
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from utils.db_api.db_core import *
from data.data_list import list_
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


@dp.callback_query_handler(text="SSS1", state="*")
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


@dp.callback_query_handler(text="SSS2", state="*")
async def three(call: CallbackQuery, state: FSMContext):
    inline_keyboard = InlineKeyboardMarkup(row_width=1)

    for group in read_all_groups():
        button = InlineKeyboardButton(text=group.group, callback_data=f"group_{group.group}")
        inline_keyboard.insert(button)
    await call.message.answer(text="Mavjud guruhlar", reply_markup=inline_keyboard)


@dp.callback_query_handler(lambda call: call.data.startswith("group_"), state="*")
async def three(call: CallbackQuery, state: FSMContext):
    await state.update_data({"group": call.data})
    print(call.data[6:])
    data = await state.get_data()
    print(bool(read_teachers(str(data['group'][6:]))))
    teacher_buttons = []
    if bool(read_teachers(data['group'][6:])) is False:
        teacher_buttons.append([InlineKeyboardButton(text="O'qituvchi qo'shish", callback_data="teacher_one")])
        teacher_buttons.append([InlineKeyboardButton(text="O'qituvchini o'chirish", callback_data="teacher_two")])
        teacher_buttons.append([InlineKeyboardButton(text="Ortga", callback_data="teacher_back")])
        teacher_markup = InlineKeyboardMarkup(inline_keyboard=teacher_buttons)
        await call.message.answer(text="Bu guruhga hozirda o'qituvchi qo'shilmagan!", reply_markup=teacher_markup)
    elif read_teachers(data['group'][6:]):
        for teacher_ in read_teachers(data['group'][6:]):
            teacher_buttons.append(
                [InlineKeyboardButton(text=teacher_.name, callback_data=f"teacher_{teacher_.teacher_id}"), ])
        teacher_buttons.append([InlineKeyboardButton(text="O'qituvchi qo'shish", callback_data="teacher_one")])
        teacher_buttons.append([InlineKeyboardButton(text="O'qituvchini o'chirish", callback_data="teacher_two")])
        teacher_buttons.append([InlineKeyboardButton(text="Ortga", callback_data="back_teacher")])
        teacher_markup = InlineKeyboardMarkup(inline_keyboard=teacher_buttons)
        await call.message.answer(f"{data['group'][6:]} guruh o'qituvchilari", reply_markup=teacher_markup)


@dp.callback_query_handler(lambda call: call.data.startswith("teacher_"), state="*")
async def teacher(call: CallbackQuery, state: FSMContext):
    await state.update_data({"teacher": call.data})
    data = await state.get_data()
    teacher_buttons = []
    if call.data == "teacher_one":
        await call.message.answer("Mavjud o'qituvchilar", reply_markup=choose_a_teacher_)
    elif call.data == "teacher_two":
        for teacher_ in read_teachers(data['group'][6:]):
            print(teacher_.teacher_id)
            teacher_buttons.append(
                [InlineKeyboardButton(text=teacher_.name, callback_data=f"delete_teacher_{teacher_.teacher_id}"), ])
        await call.message.answer("Tanlangan o'qituvchi o'chiriladi!",
                                  reply_markup=InlineKeyboardMarkup(inline_keyboard=teacher_buttons),
                                  allow_sending_without_reply=True)
    elif call.data == "teacher_back":
        await call.message.answer("Ortga", reply_markup=configuration)


@dp.callback_query_handler(lambda call: call.data.startswith("choose_"), state="*")
async def teacher(call: CallbackQuery, state: FSMContext):
    await state.update_data({"choose": call.data})
    data = await state.get_data()
    print(data['group'][6:], data['choose'][7:], list_[int(data['choose'][7:])], '------',
          read_teachers(data["group"][6:]), list_[int(data['choose'][7:])])
    if call.data.startswith("choose_"):
        if list_[int(data['choose'][7:])] not in [teacher_.name for teacher_ in read_teachers(data['group'][6:])]:
            create_teacher(group_id=data['group'][6:], name=list_[int(data['choose'][7:])],
                               teacher_id=data['choose'][7:])
            await call.message.answer("O'qituvchi muvaffaqiyatli qo'shildi!", reply_markup=configuration)
        elif list_[int(data['choose'][7:])] in [teacher_.name for teacher_ in read_teachers(data['group'][6:])]:
            await call.message.answer("Bu guruhga o'qituvchi qo'shilgan!", reply_markup=configuration)


@dp.callback_query_handler(lambda call: call.data.startswith("delete_teacher_"), state="*")
async def teacher(call: CallbackQuery, state: FSMContext):
    await state.update_data({"delete_teacher": call.data})
    data = await state.get_data()
    delete_teacher(data['delete_teacher'][15:], data["group"][6:])
    await call.message.answer("O'qituvchi muvaffaqiyatli o'chirildi!", reply_markup=configuration)


@dp.callback_query_handler(lambda call: call.data.startswith("back_teacher"), state="*")
async def teacher(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Xizmat turini tanlang!", reply_markup=configuration)
