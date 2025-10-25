from aiogram import types
from loader import dp,bot
from keyboards.default.buttons import *
from keyboards.inline.buttons import CheckCallback
@dp.callback_query(CheckCallback.filter())
async def checkme(call:types.CallbackQuery,callback_data:CheckCallback):
    status = callback_data.status
    language = callback_data.language
    telegram_id = callback_data.telegram_id
    if status=='ok':
        if language=='uz':
            await bot.send_message(chat_id=telegram_id,text="✅ Buyurtma qabul qilindi!")
        else:
            await bot.send_message(chat_id=telegram_id, text="✅ Заказ получен!")
    else:
        if language=='uz':
            await bot.send_message(chat_id=telegram_id,text="❌ Buyurtma rad etildi!")
        else:
            await bot.send_message(chat_id=telegram_id, text="❌Заказ отклонен!")
    await call.message.delete()