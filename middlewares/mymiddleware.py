from aiogram import BaseMiddleware, types
from aiogram.dispatcher.event.handler import HandlerObject
from aiogram.utils.keyboard import InlineKeyboardBuilder,InlineKeyboardButton
from aiogram.types import Message,Update
from typing import *
from loader import bot
from utils.misc.subscription import check
from api import get_all_channels,delete_channel
from aiogram.fsm.context import FSMContext
from aiogram.filters.callback_data import CallbackData
import os
class CheckSubscriptionCallback(CallbackData,prefix='ikb3'):
    check:bool
DEFAULT_RATE_LIMIT = .1
class UserCheckMiddleware(BaseMiddleware):
    async def __call__(self, handler, event: Update, data):
        user_id = event.from_user.id
        final_status = True
        builder = InlineKeyboardBuilder()
        CHANNELS = get_all_channels()
        if CHANNELS:
            for CHANNEL in CHANNELS:
                status = True
                try:
                    status = await check(user_id=user_id, channel=CHANNEL['channel_id'])
                except:
                    pass
                final_status*=status
                try:
                    channel = await bot.get_chat(CHANNEL['channel_id'])
                    try:
                        if status:
                            builder.button(text=f"✅ {channel.title}", url=f"{await channel.export_invite_link()}")
                        else:
                            builder.button(text=f"❌ {channel.title}", url=f"{await channel.export_invite_link()}")
                    except Exception as e:
                        pass
                except:
                    delete_channel(CHANNEL['channel_id'])
            text = "Obunani tekshirish"
            builder.button(text=text, callback_data=CheckSubscriptionCallback(check=True))
            builder.adjust(1)
            if not final_status:
                await bot.send_message(chat_id=user_id, text="Iltimos bot to'liq ishlashi uchun quyidagi kanallarga obuna bo'ling!", reply_markup=builder.as_markup())
            else:
                return await handler(event, data)
        else:
            return await handler(event, data)

