from loader import dp,bot
from aiogram import types,F
@dp.chat_member()
async def test(message:types.Message):
    print(message.json())
    if message.new_chat_member.status !='left':
       try:
           data = await bot.send_message(text="✅", chat_id=message.new_chat_member.user.id)
           await bot.delete_message(chat_id=message.new_chat_member.user.id,message_id=data.message_id-1)
       except:
           pass