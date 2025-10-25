from loader import dp,bot
from  aiogram import types,F
from filters import *
from aiogram.filters import Command
from keyboards.default.buttons import *
from api import get_all_users
import os
@dp.message(Command('admin'),IsChatAdmin(),IsPrivate())
async def start_admin_panel(message:types.Message):
    await message.answer("🔝 Admin panel!",reply_markup=admin_button())
@dp.message(F.text=='🗣 Reklama yuborish',IsChatAdmin(),IsPrivate())
async def get_add_type(message:types.Message):
    await message.answer("Qaysi turdagi xabar yuborasiz!\n"
                         "Tanlang👇",reply_markup=add_type())
# Back Button
@dp.message(F.text=='⏺ Bekor qilish',IsChatAdmin(),IsPrivate())
async def get_add_type(message:types.Message):
    await message.answer("Qaysi turdagi xabar yuborasiz!\n"
                         "Tanlang👇",reply_markup=add_type())
@dp.message(F.text=='🆗 Kerakmas',IsChatAdmin(),IsPrivate())
async def get_add_type(message:types.Message):
    await message.answer("Qaysi turdagi xabar yuborasiz!\n"
                         "Tanlang👇",reply_markup=add_type())
@dp.message(F.text=='📊 Obunachilar soni',IsChatAdmin(),IsPrivate())
async def get_add_type(message:types.Message):
    count = len(get_all_users())
    await message.answer(f"Bot hozir {count} ta faol obunachi bor!")


@dp.message(Command('clear'),IsChatAdmin(),IsPrivate())
async def clear(message:types.Message):
    try:
        import os
        for filename in os.listdir():
            if filename.endswith(('.mp4', '.avi', '.mkv', '.mov','.mp3','.webm','.webm.part')):
                    os.remove(filename)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    await message.answer('Kesh tozalandi!',reply_markup=types.ReplyKeyboardRemove())
@dp.message(Command('folder'),IsChatAdmin(),IsPrivate())
async def folder(message:types.Message):
    text = str(os.listdir())
    await message.answer(text,reply_markup=types.ReplyKeyboardRemove())
