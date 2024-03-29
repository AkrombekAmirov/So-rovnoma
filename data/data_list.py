list_ = ["BOBOYEVA MOHIM SHUKUROVNA", "O‘KTAMOVA YAQUTOY RAVSHAN QIZI", "SULTANOV G‘AYRAT SHARIFOVICH",
         "XUDOYBERDIYEVA VILOYAT JABBOROVNA", "YODGOROV MUHAMMAD FURQAT O‘G‘LI", "YUNUSXODJAYEV ZAIR SHAKIROVICH",
         "KADIROVA NILUFAR KAZIM QIZI", "AXMEDOV ISMAIL RIZAYEVICH"]


async def get_question_text(index):
    questions = [
        "O‘qituvchi talabalar bilan qanchalik yaxshi muloqot qiladi?",
        "O‘qituvchi o‘zining fani bo‘yicha qanchalik ma’lumotga ega?",
        "O‘qituvchining pedagogik maxoratini qanday deb bilasiz?",
        "O‘qituvchining dars jarayoniga jiddiy qarashini, darslarning o‘z vaqtida tashkillashtirilishi haqida qanday fikrdasiz?",
        "O‘qituvchi dars jarayonida darsga taaluqli bo‘lmagan mavzuda suhbatlashadimi?",
        "O‘qituvchi qanchalik pedagogik qoidalarni va shaxsiy chegaralarni buzadi, talabalarning shaxsiyatiga tegadi?",
        "O‘qituvchining talabalar bilan darsdan tashqari muloqotiga (to‘garak, tadbir, o‘zlashtirishi past o‘quvchilar, ustoz-shogird, sport) munosabatingiz?",
        "O‘qituvchining talabalarni darsga qiziqtirish mahorati haqida fikringiz?",
        "O‘qituvchining talabalarni baholashi haqida fikringiz?",
        "O‘qituvchi dars jarayonida interfaol metodlardan (klaster, aqliy xujum, guruhlarda ishlash va hk) qanchalik foydalanadi?",
        "O‘qituvchi dars jarayonida zamonaviy texnologiyalardan (masalan, smart doska, kompyuter, onlayn resurslar) qanchalik samarali foydalanadi?",
        "Umuman olganda, o‘qituvchi haqida qanday fikrdasiz?"
    ]
    return questions[index]
