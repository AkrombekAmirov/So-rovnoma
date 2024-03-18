from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline import choose_, choose_a_teacher
from data.config import ADMINS
from aiogram import types

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    print(message.from_user.id, "=========", ADMINS)
    if str(message.from_user.id) == str(ADMINS):
        await message.answer(text="Anonim berilgan baxo natijalarini bilish uchun o'qituvchini tanlang!", reply_markup=choose_a_teacher)
    elif str(message.from_user.id) != str(ADMINS):
        await message.answer(
            f"Mehnat va ijtimoiy muunosabatlar akademiyasining professor o'qituvchilarning pedagogik faoliyatiga baxo berishni boshlash uchun quyidagi tugmani bosing.",
            reply_markup=choose_)
