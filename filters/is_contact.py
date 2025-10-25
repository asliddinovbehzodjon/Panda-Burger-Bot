from aiogram.filters import Filter
from aiogram import types
from data.config import ADMINS
class IsTrueContact(Filter):
    async def __call__(self, message: types.Message) -> bool:
        try:
            return message.contact.user_id==message.from_user.id
        except:
            return False