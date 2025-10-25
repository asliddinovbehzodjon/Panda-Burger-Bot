from typing import Union
from aiogram import Bot
from loader import bot
async def check(user_id, channel: Union[str,int]):
    member = await bot.get_chat_member(chat_id=channel,user_id=user_id)
    if member.status=='left':
        return False
    else:
        return True