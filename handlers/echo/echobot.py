from loader import dp
from aiogram import types,F
from filters import IsPrivate
@dp.message(IsPrivate())
async def echo_bot(message:types.Message):
    await message.answer("Tushunarsiz buyruq!")
