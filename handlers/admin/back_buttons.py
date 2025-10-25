from loader import dp,bot
from  aiogram import types,F
from filters import *
from keyboards.default.buttons import *
from states.mystate import *
@dp.message(F.text=='◀️ Orqaga',AddChannelState.id,IsPrivate())
async def start_admin_panel(message:types.Message):
    await message.answer("🔝 Admin panel!",reply_markup=admin_button())
@dp.message(F.text=='◀️ Orqaga',AddChannelState.check,IsPrivate())
async def start_admin_panel(message:types.Message):
    await message.answer("🔝 Admin panel!",reply_markup=admin_button())
@dp.message(F.text=='⬅️ Orqaga',IsChatAdmin(),IsPrivate())
async def start_admin_panel(message:types.Message):
    await message.answer("🔝 Admin panel!",reply_markup=admin_button())
@dp.message(F.text=='◀️ Orqaga',IsChatAdmin(),IsPrivate())
async def get_add_type(message:types.Message):
    await message.answer("Qaysi turdagi xabar yuborasiz!\n"
                         "Tanlang👇",reply_markup=add_type())