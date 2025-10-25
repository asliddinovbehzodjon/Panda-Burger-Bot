from aiogram import Bot,Dispatcher
from data.config import BOT_TOKEN
from aiogram.fsm.storage.memory import MemoryStorage
bot=Bot(token=BOT_TOKEN,parse_mode='HTML')
dp=Dispatcher(storage=MemoryStorage())
