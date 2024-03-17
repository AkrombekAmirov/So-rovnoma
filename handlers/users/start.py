from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import ADMINS
from keyboards.inline import choose_

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if message.from_user.id == ADMINS:
        return
    else:
        await message.answer(
            f"Mehnat va ijtimoiy muunosabatlar akademiyasining professor o'qituvchilarning pedagogik faoliyatiga baxo berishni boshlash uchun quyidagi tugmani bosing.",
            reply_markup=choose_)
