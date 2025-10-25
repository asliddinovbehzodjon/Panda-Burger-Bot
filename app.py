import handlers,middlewares
from loader import dp,bot
import asyncio
from utils.notify_admins import start,shutdown
from middlewares.mymiddleware import UserCheckMiddleware
# Info
import logging
from utils.set_botcommands import private_chat_commands
import sys
async def main():
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await private_chat_commands()
        dp.startup.register(start)
        dp.shutdown.register(shutdown)
        dp.message.middleware(UserCheckMiddleware())
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
if __name__=='__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())