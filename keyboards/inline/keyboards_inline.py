from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

choose_ = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Xa", callback_data="123"),
    ],
])

choose_two = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Xa", callback_data="choese_yes"),
    ],
    [
        InlineKeyboardButton(text="Yoq", callback_data="choese_no"),
    ],
])

choose_a_teacher = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="BOBOYEVA MOHIM SHUKUROVNA", callback_data="1"),
    ],
    [
        InlineKeyboardButton(text="O‘KTAMOVA YAQUTOY RAVSHAN QIZI", callback_data="2"),
    ],
    [
        InlineKeyboardButton(text="SULTANOV G‘AYRAT SHARIFOVICH", callback_data="3"),
    ],
    [
        InlineKeyboardButton(text="XUDOYBERDIYEVA VILOYAT JABBOROVNA", callback_data="4"),
    ],
    [
        InlineKeyboardButton(text="YODGOROV MUHAMMAD FURQAT O‘G‘LI", callback_data="5"),
    ],
    [
        InlineKeyboardButton(text="YUNUSXODJAYEV ZAIR SHAKIROVICH", callback_data="6"),
    ],
    [
        InlineKeyboardButton(text="KADIROVA NILUFAR KAZIM QIZI", callback_data="7"),
    ],
    [
        InlineKeyboardButton(text="AXMEDOV ISMAIL RIZAYEVICH", callback_data="8"),
    ],

])
choose_a_teacher_ = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="BOBOYEVA MOHIM SHUKUROVNA", callback_data="choose_0"),
    ],
    [
        InlineKeyboardButton(text="O‘KTAMOVA YAQUTOY RAVSHAN QIZI", callback_data="choose_1"),
    ],
    [
        InlineKeyboardButton(text="SULTANOV G‘AYRAT SHARIFOVICH", callback_data="choose_2"),
    ],
    [
        InlineKeyboardButton(text="XUDOYBERDIYEVA VILOYAT JABBOROVNA", callback_data="choose_3"),
    ],
    [
        InlineKeyboardButton(text="YODGOROV MUHAMMAD FURQAT O‘G‘LI", callback_data="choose_4"),
    ],
    [
        InlineKeyboardButton(text="YUNUSXODJAYEV ZAIR SHAKIROVICH", callback_data="choose_5"),
    ],
    [
        InlineKeyboardButton(text="	KADIROVA NILUFAR KAZIM QIZI", callback_data="choose_6"),
    ],
    [
        InlineKeyboardButton(text="AXMEDOV ISMAIL RIZAYEVICH", callback_data="choose_7"),
    ],
])
configuration = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Guruh yaratish", callback_data="SSS1"),
    ],
    [
        InlineKeyboardButton(text="Guruhlarni ko'rish", callback_data="SSS2"),
    ],
])

teacher = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="O'qituvchi qo'shish", callback_data="teacher_one"),
    ],
    [
        InlineKeyboardButton(text="O'qituvchini o'chirish", callback_data="teacher_two"),
    ],
])

question_one = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="a'lo", callback_data="5"),
    ],
    [
        InlineKeyboardButton(text="yaxshi", callback_data="4"),
    ],
    [
        InlineKeyboardButton(text="o'rtacha", callback_data="3"),
    ],
    [
        InlineKeyboardButton(text="qoniqarsiz", callback_data="2"),
    ],
])

question_two = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Ko‘p narsani biladi", callback_data="5"),
    ],
    [
        InlineKeyboardButton(text="Faqat mavzu bo‘yicha biladi", callback_data="4"),
    ],
    [
        InlineKeyboardButton(text="Biroz bilimli", callback_data="3"),
    ],
    [
        InlineKeyboardButton(text="Baxolay olmayman", callback_data="2"),
    ],
])

question_three = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Yuqori mahoratli", callback_data="5"),
    ],
    [
        InlineKeyboardButton(text="O‘rtacha mahoratli", callback_data="4"),
    ],
    [
        InlineKeyboardButton(text="Qoniqarli darajada", callback_data="3"),
    ],
    [
        InlineKeyboardButton(text="Baholay olmayman", callback_data="2"),
    ],
])

question_four = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Talabchan va qattiqqo‘l", callback_data="5"),
    ],
    [
        InlineKeyboardButton(text="Talabchan va o‘z vaqtida", callback_data="4"),
    ],
    [
        InlineKeyboardButton(text="Biroz talabchan va jiddiy", callback_data="3"),
    ],
    [
        InlineKeyboardButton(text="Mas’uliyatsiz va tartibsiz", callback_data="2"),
    ],
])

question_five = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Ha, doimiy", callback_data="5"),
    ],
    [
        InlineKeyboardButton(text="Ba’zi holatlarda", callback_data="4"),
    ],
    [
        InlineKeyboardButton(text="Kamdan kam", callback_data="3"),
    ],
    [
        InlineKeyboardButton(text="Yo‘q,umuman", callback_data="2"),
    ],
])

question_six = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Madaniyatli munosabatda", callback_data="5"),
    ],
    [
        InlineKeyboardButton(text="Talabalar shaxsiyatini hurmat qiladi", callback_data="4"),
    ],
    [
        InlineKeyboardButton(text="Talabalar shaxsiyatini hurmat qilmaydi", callback_data="3"),
    ],
    [
        InlineKeyboardButton(text="Talabalar shaxsiyatiga tegadi", callback_data="2"),
    ],
])

question_eight = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Juda qiziqarli", callback_data="5"),
    ],
    [
        InlineKeyboardButton(text="O‘rtacha qiziqarli", callback_data="4"),
    ],
    [
        InlineKeyboardButton(text="Qoniqarli darajada", callback_data="3"),
    ],
    [
        InlineKeyboardButton(text="Baholay olmayman", callback_data="2"),
    ],
])

question_nine = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Adolatli", callback_data="5"),
    ],
    [
        InlineKeyboardButton(text="Tanish-bilishchilikka yo‘l qo‘yadi", callback_data="4"),
    ],
    [
        InlineKeyboardButton(text="Shaxsiy xusumatni aralashtiradi", callback_data="3"),
    ],
    [
        InlineKeyboardButton(text="Adolatsiz", callback_data="2"),
    ],
])

question_ten = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="To‘liq foydalanadi", callback_data="5"),
    ],
    [
        InlineKeyboardButton(text="Qisman foydalanadi", callback_data="4"),
    ],
    [
        InlineKeyboardButton(text="Kamdan-kam foydalanadi", callback_data="3"),
    ],
    [
        InlineKeyboardButton(text="Umuman foydalanmaydi", callback_data="2"),
    ],
])
