from loader import dp,bot
from api import *
from aiogram import types,F
from keyboards.default.buttons import settings
@dp.message(F.text.in_(["⚙️ Настройки","⚙️ Sozlamalar"]))
async def start_settings(message:types.Message):
    user = get_user(telegram_id=message.from_user.id)
    if user != 'Not Found':
        language = user.get('language', 'uz')
    else:
        language = 'uz'
    if language == 'ru':
        await message.answer(f"⚙️  Добро пожаловать в раздел настроек!\n\n"
                             f"🇺🇿/🇷🇺 Вы можете изменить язык с помощью кнопок.", reply_markup=settings(language))
    else:
        await message.answer("⚙️ Sozlamalar bo'limiga xush kelibsiz!\n\n"
                             "🇺🇿/🇷🇺 Tugmachalar orqali tilni o'zgartirishingiz mumkin.",
                             reply_markup=settings(language))