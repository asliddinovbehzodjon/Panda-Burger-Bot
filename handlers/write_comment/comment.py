import asyncio

from aiogram.fsm.context import FSMContext
from loader import dp,bot
from aiogram import types,F,html
from keyboards.default.buttons import *
from data.config import ADMINS
from aiogram.filters.state import State,StatesGroup
from keyboards.inline.buttons import *
from api import *
###### State For Comment ###########
class Comment(StatesGroup):
    text = State()
###################################
######## Write Comment Button Type ##################
@dp.message(F.text.in_(["✍️ Sharh qoldiring","✍️ Оставить отзыв"]))
async def begin(message:types.Message,state:FSMContext):
    user = get_user(telegram_id=message.from_user.id)
    if user != 'Not Found':
        language = user.get('language', 'uz')
    else:
        language = 'uz'
    if language=='uz':
        await message.answer("🙂 Bizga bo'lgan biror fikringiz yoki taklifingiz bo'lsa yozib qoldiring. Sizning fikringiz biz uchun fikringiz muhim!",reply_markup=cancel(language))
        await state.set_state(Comment.text)
    else:
        await message.answer("🙂 Если у вас есть какие-либо замечания или предложения для нас, пожалуйста, напишите их. Ваше мнение важно для нас!",reply_markup=cancel(language))
        await state.set_state(Comment.text)
######### Write Comment ##############
@dp.message(F.text,Comment.text)
async def comment_get(message:types.Message,state:FSMContext):
    user = get_user(telegram_id=message.from_user.id)
    if user != 'Not Found':
        language = user.get('language', 'uz')
    else:
        language = 'uz'
    if message.text in ["❌ Отменить","❌ Bekor qilish"]:
        if language == "uz":
            await message.answer("✅ Bosh menyuga xush kelibsiz!\n" \
                                 f"🍕 Mazali pitsalar! Buyurtma berishni boshlaysizmi?", reply_markup=main_button(language))
        else:
            await message.answer(f"✅ Добро пожаловать в главное меню!\n" \
                                 f"🍕 Вкусные пиццы! Вы начинаете заказывать?", reply_markup=main_button(language))
        await state.clear()
    else:

        text=message.text
        link = f"tg://user?id={message.from_user.id}"
        text_ru = (f"👤 Отправитель: {html.link(value=message.from_user.full_name,link=link)}\n"
                   f"📝 Сообщение: {text}")
        text_uz = (f"👤 Yuboruvchi: {html.link(value=message.from_user.full_name,link=link)}\n"
                   f"📝 Xabar: {text}")
        if language=='uz':
            try:
                for i in ADMINS:
                    await bot.send_message(text=text_uz, chat_id=i,
                                           reply_markup=comment_button(telegram_id=message.from_user.id,
                                                                       language=language))
            except Exception as e:
                    print(e)
                    pass
        else:
            try:
                for i in ADMINS:
                    await bot.send_message(text=text_ru, chat_id=i,
                                           reply_markup=comment_button(telegram_id=message.from_user.id,
                                                                       language=language))
            except Exception as e:
                print(e)
                pass
        if language == "uz":
            await message.answer("😇 Fikringiz uchun rahmat!")
            await message.answer("✅ Bosh menyuga xush kelibsiz!\n" \
                                 f"🍕 Mazali pitsalar! Buyurtma berishni boshlaysizmi?", reply_markup=main_button(language))
        else:
            await message.answer("😇 Спасибо за ваш отзыв!")
            await message.answer(f"✅ Добро пожаловать в главное меню!\n" \
                                 f"🍕 Вкусные пиццы! Вы начинаете заказывать?", reply_markup=main_button(language))
        await state.clear()
@dp.callback_query(CommentCallback.filter())
async def short_answer(call:types.CallbackQuery,callback_data:CommentCallback):
    await call.answer(cache_time=60)
    telegram_id = callback_data.telegram_id
    language = callback_data.language
    text_uz="⭐️⭐️⭐️\nSalom.Izoh adminlar tomonidan ko'rildiAjoyib!Buni albatta inobatga olamiz!\n⭐️⭐️⭐️"
    text_ru='⭐️⭐️⭐️\nЗдравствуйте.Комментарий просмотрен администраторомОтлично!Мы обязательно примем это во внимание!\n⭐️⭐️⭐️'
    try:
        await bot.send_message(text=text_uz if language == 'uz' else text_ru, chat_id=telegram_id
                               )
        data = await call.message.answer("Xabar yuborildi!")
    except:
        data = await call.message.answer("Xabar yuborilmadi!")
        pass
    await call.message.delete()
    await asyncio.sleep(5)
    await data.delete()