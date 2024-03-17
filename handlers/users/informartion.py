from file_service.file_write import file_read, check_passport1, update_person_info
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
from keyboards.inline import *
from aiogram import types
from loader import dp
from states import *

list_ = ["BOBOYEVA MOHIM SHUKUROVNA", "O‘KTAMOVA YAQUTOY RAVSHAN QIZI", "SULTANOV G‘AYRAT SHARIFOVICH",
         "XUDOYBERDIYEVA VILOYAT JABBOROVNA", "YODGOROV MUHAMMAD FURQAT O‘G‘LI", "YUNUSXODJAYEV ZAIR SHAKIROVICH",
         "	KADIROVA NILUFAR KAZIM QIZI"]


async def get_next_teacher(state: FSMContext):
    async with state.proxy() as data:
        numbers = data.get("number", 0)
        numbers += 1
        data["number"] = numbers
        return numbers


number = 0


@dp.callback_query_handler(text='1')
async def get_one(call: types.CallbackQuery, state=FSMContext):
    await state.update_data({"number": 0})
    await call.message.delete()
    await call.message.answer(
        f"Mehnat va ijtimoiy muunosabatlar akademiyasi <b><u>{list_[0]}</u></b> ning pedagogik faoliyatiga baxo bering.\nO‘qituvchi talabalar bilan qanchalik yaxshi muloqot qiladi?",
        reply_markup=question_one, parse_mode="HTML")
    await Question.one.set()


@dp.callback_query_handler(state=Question.one)
async def get_two(call: types.CallbackQuery, state: FSMContext):
    await state.update_data({"one": call.data})
    await call.message.delete()
    print(await check_passport1(name=list_[0]))
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
    data = await state.get_data()
    number = data.get("number")
    data2 = await check_passport1(name=list_[data.get("number")])
    print(data2, "\n", data, "\n", data2[1:11])
    print(sum([int(item) for item in data2[1:11]]))
    sonlar = [int(value) for key, value in data.items() if key != 'twelve' or key != 'number']
    print(sum(sonlar))
    list1 = [int(value) for key, value in data.items()]
    print(list1, list1[1:11], sum(list1[1:11]))
    data1 = [[list_[data.get("number")], f"{int(data.get('one')) + int(data2[1])}", f"{int(data.get('two')) + int(data2[2])}",
              f"{int(data.get('three')) + int(data2[3])}", f"{int(data.get('four')) + int(data2[4])}",
              f"{int(data.get('five')) + int(data2[5])}", f"{int(data.get('six')) + int(data2[6])}",
              f"{int(data.get('seven')) + int(data2[7])}", f"{int(data.get('eight')) + int(data2[8])}",
              f"{int(data.get('nine')) + int(data2[9])}", f"{int(data.get('ten')) + int(data2[10])}",
              f"{int(data.get('eleven')) + int(data2[11])}", f"{int(data2[12]) + 60}",
              f"{int(data2[13]) + int(sum(list1[1:11]))}"]]
    await update_person_info((list_[data.get("number")]), data1)
    if len(list_) == data.get("number") + 1:
        await call.message.answer("Siz barcha baxolaringiz muvaffaqiyatli qabul qilindi.\nBaxo berish tugadi!\n/start")
    elif len(list_) != data.get("number"):
        await call.message.answer(
            f"Siz {list_[number]} ga bergan baxoingiz muvaffaqiyatli qabul qilindi.\n Baxo berishda davom etasizmi?",
            reply_markup=choose_)
        await state.update_data({"number": await get_next_teacher(state)})
    await Question.next()


@dp.callback_query_handler(state=Question.thirteen)
async def get_thirteen(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await call.message.delete()
    await call.message.answer(f"<b><u>{list_[data.get('number')]}</u></b>\n")
    await call.message.answer(
        "Professor-o‘qituvchining talabalar bilan qanchalik yaxshi muloqot qiladi?",
        reply_markup=question_one, parse_mode="HTML")
    await Question.one.set()
