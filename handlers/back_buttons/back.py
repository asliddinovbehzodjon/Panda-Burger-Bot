from aiogram import types,F
from loader import dp
from api import *
from keyboards.default.buttons import main_button
start_text_uz = '''
✅ Bosh menyuga xush kelibsiz!
🍕 Mazali pitsalar! Buyurtma berishni boshlaysizmi?
'''
start_text_ru = '''
✅ Добро пожаловать в главное меню!
🍕 Вкусные пиццы! Вы начинаете заказывать?
'''
@dp.message(F.text.in_(["🔝 Bosh menyuga qaytish","🔝 Вернуться в главное меню"]))
async def back_btn(message:types.Message):
    user = get_user(telegram_id=message.from_user.id)
    if user != 'Not Found':
        language = user.get('language', 'uz')
    else:
        language = 'uz'
    if language == 'uz':
        await message.answer(text=start_text_uz, reply_markup=main_button(language))
    else:
        await message.answer(text=start_text_ru, reply_markup=main_button(language))