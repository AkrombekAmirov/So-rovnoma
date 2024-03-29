from file_service.file_write import file_read, check_passport1, update_person_info, read_student
from aiogram.dispatcher.filters.builtin import CommandStart
from data.data_list import list_, get_question_text
from aiogram.dispatcher import FSMContext
from utils.db_api.db_core import *
from keyboards.inline import *
from aiogram import types
from loader import dp
from states import *


@dp.message_handler(commands=['exit'])
async def exit_system(message: types.Message, state: FSMContext):
    await state.finish()  # Holatni tozalash
    await message.answer("Tizimdan muvaffaqiyatli chiqib kettiz. Iltimos, qaytadan kiriting:")
    await Question.hemis_id.set()


@dp.message_handler(commands=["start"])
async def get_func(message: types.Message, state: FSMContext):
    await message.answer(
        f"Mehnat va ijtimoiy muunosabatlar akademiyasining professor o'qituvchilarning pedagogik faoliyatiga baxo berishni boshlash uchun HEMIS id ni kiriting!")
    await message.delete()
    await Question.hemis_id.set()


@dp.message_handler(state=Question.hemis_id)
async def get_one(message: types.Message, state=FSMContext):
    print(await read_student(message.text))
    if bool(get_student(message.text)) is True:
        await message.answer(text="Faqat bir marotaaba baxo berish mumkin! Iltimos qaytadan boshqa HEMIS id kiritib ko'ring")
        await Question.hemis_id.set()
    elif await read_student(message.text):
        data = await read_student(message.text)
        # print(int([teacher_.teacher_id for teacher_ in read_teachers(data[2])][1]), 'llllllllll', len([teacher_.teacher_id for teacher_ in read_teachers(data[2])]))
        await state.update_data({"hemis_id": message.text})
        await state.update_data({"number": int([teacher_.teacher_id for teacher_ in read_teachers(data[2])][0])})
        create_student(hemis_id=message.text, group_id=data[2], name=data[1], telegram_id=message.from_user.id,
                       username=message.from_user.username)
        s = await state.get_data()
        # print(s, "pppppppppppppppppppp", int([teacher_.teacher_id for teacher_ in read_teachers(data[2])][1]))
        # print(int([teacher_.teacher_id for teacher_ in read_teachers(data[2])][0]), "pppppppppppppppppppp", data[2])
        await message.answer(
            f"Mehnat va ijtimoiy muunosabatlar akademiyasi <b><u>{list_[int([teacher_.teacher_id for teacher_ in read_teachers(data[2])][0])]}</u></b> ning pedagogik faoliyatiga baxo bering.\n{await get_question_text(0)}",
            reply_markup=question_one, parse_mode="HTML")
        await Question.next()
    else:
        await message.answer("Hemis id noto'g'ri kiritildi. Iltimos qaytadan kiriting!")
        await Question.hemis_id.set()


@dp.callback_query_handler(state=Question.one)
async def get_two(call: types.CallbackQuery, state: FSMContext):
    await state.update_data({"one": call.data})
    await call.message.delete()
    await call.message.answer(text=await get_question_text(1), reply_markup=question_two)
    await Question.next()


@dp.callback_query_handler(state=Question.two)
async def get_three(call: types.CallbackQuery, state: FSMContext):
    await state.update_data({"two": call.data})
    await call.message.delete()
    await call.message.answer(text=await get_question_text(2), reply_markup=question_three)
    await Question.next()


@dp.callback_query_handler(state=Question.three)
async def get_four(call: types.CallbackQuery, state: FSMContext):
    await state.update_data({"three": call.data})
    await call.message.delete()
    await call.message.answer(text=await get_question_text(3), reply_markup=question_four)
    await Question.next()


@dp.callback_query_handler(state=Question.four)
async def get_five(call: types.CallbackQuery, state: FSMContext):
    await state.update_data({"four": call.data})
    await call.message.delete()
    await call.message.answer(text=await get_question_text(4), reply_markup=question_five)
    await Question.next()


@dp.callback_query_handler(state=Question.five)
async def get_six(call: types.CallbackQuery, state: FSMContext):
    await state.update_data({"five": call.data})
    await call.message.delete()
    await call.message.answer(text=await get_question_text(5), reply_markup=question_six)
    await Question.next()


@dp.callback_query_handler(state=Question.six)
async def get_seven(call: types.CallbackQuery, state: FSMContext):
    await state.update_data({"six": call.data})
    await call.message.delete()
    await call.message.answer(text=await get_question_text(6), reply_markup=question_one)
    await Question.next()


@dp.callback_query_handler(state=Question.seven)
async def get_eight(call: types.CallbackQuery, state: FSMContext):
    await state.update_data({"seven": call.data})
    await call.message.delete()
    await call.message.answer(text=await get_question_text(7), reply_markup=question_eight)
    await Question.next()


@dp.callback_query_handler(state=Question.eight)
async def get_nine(call: types.CallbackQuery, state: FSMContext):
    await state.update_data({"eight": call.data})
    await call.message.delete()
    await call.message.answer(await get_question_text(8), reply_markup=question_nine)
    await Question.next()


@dp.callback_query_handler(state=Question.nine)
async def get_ten(call: types.CallbackQuery, state: FSMContext):
    await state.update_data({"nine": call.data})
    await call.message.delete()
    await call.message.answer(await get_question_text(9), reply_markup=question_ten)
    await Question.next()


@dp.callback_query_handler(state=Question.ten)
async def get_eleven(call: types.CallbackQuery, state: FSMContext):
    await state.update_data({"ten": call.data})
    await call.message.delete()
    await call.message.answer(await get_question_text(10), reply_markup=question_ten)
    await Question.next()


@dp.callback_query_handler(state=Question.eleven)
async def get_twelve(call: types.CallbackQuery, state: FSMContext):
    await state.update_data({"eleven": call.data})
    await call.message.delete()
    await call.message.answer(await get_question_text(11), reply_markup=question_one)
    await Question.next()


@dp.callback_query_handler(state=Question.twelve)
async def get_thirteen(call: types.CallbackQuery, state: FSMContext):
    await state.update_data({"twelve": call.data})
    await call.message.delete()
    data = await state.get_data()
    data1_ = await read_student(data.get('hemis_id'))
    data2 = await check_passport1(name=list_[data.get("number")])
    # print(data2, "\n", data, "\n", data2[1:11])
    # print(sum([int(item) for item in data2[1:11]]))
    list1 = [int(value) for key, value in data.items()]
    # print(list1, list1[2:14], sum(list1[2:14]))
    data1 = [[list_[int(data.get("number"))], f"{int(data.get('one')) + int(data2[1])}",
              f"{int(data.get('two')) + int(data2[2])}",
              f"{int(data.get('three')) + int(data2[3])}", f"{int(data.get('four')) + int(data2[4])}",
              f"{int(data.get('five')) + int(data2[5])}", f"{int(data.get('six')) + int(data2[6])}",
              f"{int(data.get('seven')) + int(data2[7])}", f"{int(data.get('eight')) + int(data2[8])}",
              f"{int(data.get('nine')) + int(data2[9])}", f"{int(data.get('ten')) + int(data2[10])}",
              f"{int(data.get('eleven')) + int(data2[11])}", f"{int(data.get('twelve')) + int(data2[12])}",
              f"{int(data2[13]) + 60}",
              f"{int(data2[14]) + int(sum(list1[2:14]))}"]]
    await update_person_info((list_[data.get("number")]), data1)
    # print(int([teacher_.teacher_id for teacher_ in read_teachers(data1_[2])][1]), 'llllllllll')
    if 1 == len([teacher_.teacher_id for teacher_ in read_teachers(data1_[2])]) or int([teacher_.teacher_id for teacher_ in read_teachers(data1_[2])][1]) == int(data.get("number")):
        await call.message.answer("Siz barcha baxolaringiz muvaffaqiyatli qabul qilindi.\nBaxo berish tugadi!\n/start")
    elif int([teacher_.teacher_id for teacher_ in read_teachers(data1_[2])][1]) != int(data.get("number")):
        await call.message.answer(
            f"Siz {list_[int(data.get('number'))]} ga bergan baxoingiz muvaffaqiyatli qabul qilindi.\n Baxo berishda davom etasizmi?",
            reply_markup=choose_)
        await state.update_data({"number": int([teacher_.teacher_id for teacher_ in read_teachers(data1_[2])][1])})
    await Question.next()


@dp.callback_query_handler(state=Question.thirteen)
async def get_thirteen(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await call.message.delete()
    await call.message.answer(f"<b><u>{list_[data.get('number')]}</u></b>\n")
    await call.message.answer(await get_question_text(0), reply_markup=question_one, parse_mode="HTML")
    await Question.one.set()
