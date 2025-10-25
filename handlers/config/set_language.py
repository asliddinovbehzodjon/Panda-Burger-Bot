from api import change_user_language
from loader import dp,bot
from aiogram.fsm.context import FSMContext
from aiogram import types,F
from api import get_user,change_user_language
from keyboards.default.buttons import language_button,main_button
from states.mystate import LanguageState
from filters import OnlyLanguageButton
from aiogram.filters import Command
@dp.message(Command('set_language'))
async def get(message:types.Message):
    await message.answer(text=
                         f"🇺🇿 Botdan foydalanish uchun o'zingizga qulay tilni tanlang.\n" \
                         f"🇷🇺 Выберите удобный для вас язык для использования бота."
                         , reply_markup=language_button())
@dp.message(OnlyLanguageButton(),LanguageState.language_get)
async def change_language(message:types.Message,state:FSMContext):
    if message.text=="🇷🇺 Pусский язык":
        change_user_language(telegram_id=message.from_user.id,language='ru')
        await message.answer(text=f"✅ Добро пожаловать в главное меню!\n"\
                             f"🍕 Вкусные пиццы! Вы начинаете заказывать?", reply_markup=main_button(language='ru'))
    else:
        change_user_language(telegram_id=message.from_user.id, language="uz")
        await message.answer(text=f"✅ Bosh menyuga xush kelibsiz!\n"\
                             f"🍕 Mazali pitsalar! Buyurtma berishni boshlaysizmi?", reply_markup=main_button(language='uz'))
    await state.clear()
@dp.message(OnlyLanguageButton())
async def change_language(message:types.Message,state:FSMContext):
    if message.text=="🇷🇺 Pусский язык":
        change_user_language(telegram_id=message.from_user.id,language='ru')
        await message.answer(text=f"✅ Добро пожаловать в главное меню!\n"\
                             f"🍕 Вкусные пиццы! Вы начинаете заказывать?", reply_markup=main_button(language='ru'))
    else:
        change_user_language(telegram_id=message.from_user.id, language="uz")
        await message.answer(text=f"✅ Bosh menyuga xush kelibsiz!\n"\
                             f"🍕 Mazali pitsalar! Buyurtma berishni boshlaysizmi?", reply_markup=main_button(language='uz'))
