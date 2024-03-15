from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline import *
from file_service.file_write import file_read
from aiogram.dispatcher import FSMContext
from aiogram import types
from loader import dp
from states import *

number = 0
list_ = ["BOBOYEVA MOHIM SHUKUROVNA", "O‘KTAMOVA YAQUTOY RAVSHAN QIZI", "SULTANOV G‘AYRAT SHARIFOVICH",
         "XUDOYBERDIYEVA VILOYAT JABBOROVNA", "YODGOROV MUHAMMAD FURQAT O‘G‘LI", "YUNUSXODJAYEV ZAIR SHAKIROVICH",
         "	KADIROVA NILUFAR KAZIM QIZI"]


@dp.message_handler(CommandStart())
async def get_one(message: types.Message):
    await message.answer(
        "Mehnat va ijtimoiy muunosabatlar akademiyasi {list_[number]} ning pedagogik faoliyatiga baxo bering.\nO‘qituvchi talabalar bilan qanchalik yaxshi muloqot qiladi?",
        reply_markup=question_one)
    await Question.one.set()


@dp.callback_query_handler(state=Question.one)
async def get_two(call: types.CallbackQuery, state: FSMContext):
    await state.update_data({"one": call.data})
    await call.message.delete()
    await call.message.answer("O‘qituvchi o‘zining fani bo‘yicha qanchalik ma’lumotga ega?", reply_markup=question_two)
    await Question.next()


@dp.callback_query_handler(state=Question.two)
async def get_three(call: types.CallbackQuery, state: FSMContext):
    await state.update_data({"two": call.data})
    await call.message.delete()
    await call.message.answer("O‘qituvchining pedagogik maxoratini qanday deb bilasiz?", reply_markup=question_three)
    await Question.next()


@dp.callback_query_handler(state=Question.three)
async def get_four(call: types.CallbackQuery, state: FSMContext):
    await state.update_data({"three": call.data})
    await call.message.delete()
    await call.message.answer(
        "O‘qituvchining dars jarayoniga jiddiy qarashini, darslarning o‘z vaqtida tashkillashtirilishi haqida qanday fikrdasiz?",
        reply_markup=question_four)
    await Question.next()


@dp.callback_query_handler(state=Question.four)
async def get_five(call: types.CallbackQuery, state: FSMContext):
    await state.update_data({"four": call.data})
    await call.message.delete()
    await call.message.answer("O‘qituvchi dars jarayonida darsga taaluqli bo‘lmagan mavzuda suhbatlashadimi?",
                              reply_markup=question_five)
    await Question.next()


@dp.callback_query_handler(state=Question.five)
async def get_six(call: types.CallbackQuery, state: FSMContext):
    await state.update_data({"five": call.data})
    await call.message.delete()
    await call.message.answer(
        "O‘qituvchi qanchalik pedagogik qoidalarni va shaxsiy chegaralarni buzadi, talabalarning shaxsiyatiga tegadi?",
        reply_markup=question_six)
    await Question.next()


@dp.callback_query_handler(state=Question.six)
async def get_seven(call: types.CallbackQuery, state: FSMContext):
    await state.update_data({"six": call.data})
    await call.message.delete()
    await call.message.answer(
        "O‘qituvchining talabalar bilan darsdan tashqari muloqotiga (to‘garak, tadbir, o‘zlashtirishi past o‘quvchilar, ustoz-shogird, sport) munosabatingiz?",
        reply_markup=question_one)
    await Question.next()


@dp.callback_query_handler(state=Question.seven)
async def get_eight(call: types.CallbackQuery, state: FSMContext):
    await state.update_data({"seven": call.data})
    await call.message.delete()
    await call.message.answer("O‘qituvchining talabalarni darsga qiziqtirish mahorati haqida fikringiz?",
                              reply_markup=question_eight)
    await Question.next()


@dp.callback_query_handler(state=Question.eight)
async def get_nine(call: types.CallbackQuery, state: FSMContext):
    await state.update_data({"eight": call.data})
    await call.message.delete()
    await call.message.answer("O‘qituvchining talabalarni baholashi haqida fikringiz?",
                              reply_markup=question_nine)
    await Question.next()


@dp.callback_query_handler(state=Question.nine)
async def get_ten(call: types.CallbackQuery, state: FSMContext):
    await state.update_data({"nine": call.data})
    await call.message.delete()
    await call.message.answer(
        "O‘qituvchi dars jarayonida interfaol metodlardan (klaster, aqliy xujum, guruhlarda ishlash va hk) qanchalik foydalanadi?",
        reply_markup=question_ten)
    await Question.next()


@dp.callback_query_handler(state=Question.ten)
async def get_eleven(call: types.CallbackQuery, state: FSMContext):
    await state.update_data({"ten": call.data})
    await call.message.delete()
    await call.message.answer(
        "O‘qituvchi dars jarayonida zamonaviy texnologiyalardan (masalan, smart doska, kompyuter, onlayn resurslar) qanchalik samarali foydalanadi?",
        reply_markup=question_ten)
    await Question.next()


@dp.callback_query_handler(state=Question.eleven)
async def get_twelve(call: types.CallbackQuery, state: FSMContext):
    await state.update_data({"eleven": call.data})
    await call.message.delete()
    await call.message.answer(
        "Umuman olganda, o‘qituvchi haqida qanday fikrdasiz?",
        reply_markup=question_one)
    await Question.next()


@dp.callback_query_handler(state=Question.twelve)
async def get_thirteen(call: types.CallbackQuery, state: FSMContext):
    await state.update_data({"twelve": call.data})
    await call.message.delete()
    global number
    await call.message.answer(f"Siz {list_[number]} ga bergan baxoingiz muvaffaqiyatli qabul qilindi.")
    number += 1
    await call.message.answer(f"{list_[number]}\n")
    await call.message.answer("Professor-o‘qituvchining talabalar bilan qanchalik yaxshi muloqot qiladi?",
                              reply_markup=question_one)
    await Question.one.set()
