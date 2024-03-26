from file_service.file_write import file_read, check_passport1, update_person_info
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
from keyboards.inline import *
from aiogram import types
from loader import dp
from states import *


@dp.callback_query_handler(lambda call: call.data in ["1", "2", "3", "4", "5", "6", "7"])
async def admin(call: types.CallbackQuery):
    name_map = {
        "1": "BOBOYEVA MOHIM SHUKUROVNA",
        "2": "O‘KTAMOVA YAQUTOY RAVSHAN QIZI",
        "3": "SULTANOV G‘AYRAT SHARIFOVICH",
        "4": "XUDOYBERDIYEVA VILOYAT JABBOROVNA",
        "5": "YODGOROV MUHAMMAD FURQAT O‘G‘LI",
        "6": "YUNUSXODJAYEV ZAIR SHAKIROVICH",
        "7": "KADIROVA NILUFAR KAZIM QIZI",
    }
    await get_teacher_info(name_map[call.data], call)
    await call.message.delete()


async def get_teacher_info(name: str, call: types.CallbackQuery):
    func_data = await check_passport1(name)
    await call.message.answer(
        f"{name} ning natijalari\nBaxo berganlar soni: {int(int(func_data[13])/60)}\nTo'planishi kerak bo'lgan baxo: {func_data[13]}\nTo'plangan baxo: {func_data[14]}\nFoiz kursatgichi: {int(int(func_data[14]) / int(func_data[13]) * 100)} %",
        reply_markup=choose_a_teacher)
