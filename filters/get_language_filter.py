from aiogram.filters import Filter
from aiogram import types
from data.config import ADMINS
class OnlyLanguageButton(Filter):
    async def __call__(self, message: types.Message) -> bool:
        if message.content_type=='text':
            if message.text in["🇺🇿 O'zbek tili","🇷🇺 Pусский язык"]:
                return True
            else:
                return False
        else:
            return False