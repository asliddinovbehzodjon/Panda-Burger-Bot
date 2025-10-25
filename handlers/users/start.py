from loader import dp,bot
from aiogram import types,F
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder,InlineKeyboardButton
from keyboards.default.buttons import language_button,main_button
from aiogram.fsm.context import FSMContext
from states.mystate import *
from api import *
import os
start_text_uz = '''
✅ Bosh menyuga xush kelibsiz!
🍕 Mazali pitsalar! Buyurtma berishni boshlaysizmi?
'''
start_text_ru = '''
✅ Добро пожаловать в главное меню!
🍕 Вкусные пиццы! Вы начинаете заказывать?
'''

@dp.message(CommandStart())
async def start_chat(message:types.Message,state:FSMContext):
    user = get_user(telegram_id=message.from_user.id)
    if user != 'Not Found':
        language = user.get('language', 'uz')
    else:
        language = 'uz'
    try:
       data =  create_user(name=message.from_user.full_name,telegram_id=message.from_user.id)
    except:
        data = ''
    if data==201:
        await message.answer(text=
                             f"🇺🇿 Botdan foydalanish uchun o'zingizga qulay tilni tanlang.\n" \
                             f"🇷🇺 Выберите удобный для вас язык для использования бота."
                             , reply_markup=language_button())
        await state.set_state(LanguageState.language_get)

    else:
        if language == 'uz':
            await message.answer(text=start_text_uz, reply_markup=main_button(language))
        else:
            await message.answer(text=start_text_ru, reply_markup=main_button(language))


