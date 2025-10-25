from loader import dp,bot
from aiogram import types,F
from keyboards.default.buttons import *
from keyboards.inline.buttons import *
from api import *
from data.config import ADMINS
from aiogram.fsm.context import FSMContext
from filters import IsTrueContact
@dp.message(F.contact,IsTrueContact())
async def get_contact_handler(message:types.Message,state:FSMContext):
    contact  = message.contact.phone_number
    user = get_user(telegram_id=message.from_user.id)
    if user != 'Not Found':
        language = user.get('language', 'uz')
    else:
        language = 'uz'
    await state.update_data(
        {'level': 'category'}
    )
    change_phone(telegram_id=message.from_user.id,phone=contact)
    text = "<b>Manzilni ulashing</b>" if language=='uz' else "<b>Поделиться адресом</b>"
    await message.answer(text,reply_markup=get_location(language))
@dp.message(F.location)
async def get_location_handler(message:types.Message,state:FSMContext):
    latitude = message.location.latitude
    longitude = message.location.longitude
    user = get_user(telegram_id=message.from_user.id)
    if user != 'Not Found':
        language = user.get('language', 'uz')
    else:
        language = 'uz'
    await state.update_data(
        {'level': 'category'}
    )
    change_address(telegram_id=message.from_user.id, latitude=latitude,longitude=longitude)
    text = "⬇️ To'lov qilish usulini tanlang" if language == 'uz' else " Выберите способ оплаты"
    await message.answer(text, reply_markup=payment_button(language))
@dp.message(F.text.in_(["Naqd","Click","Наличные"]))
async def  payment_send(message:types.Message):
    user = get_user(telegram_id=message.from_user.id)
    if user != 'Not Found':
        language = user.get('language', 'uz')
    else:
        language = 'uz'
    text = "Bot Test Rejimda Ishlayapti" if language=='uz' else "Бот работает в тестовом режиме"
    await message.answer(text=text)
    if language == "uz":
        await message.answer("✅ Bosh menyuga xush kelibsiz!\n"
                             f"🍕 Mazali pitsalar! Buyurtma berishni boshlaysizmi?", reply_markup=main_button(language))
    else:
        await message.answer(f"✅ Добро пожаловать в главное меню!\n"
                             f"🍕 Вкусные пиццы! Вы начинаете заказывать?", reply_markup=main_button(language))
    shop = shop_info(telegram_id=message.from_user.id, language=language)
    text = ''
    payment_type = message.text
    user_info = all_info(message.from_user.id)
    if user_info!={}:
        link = f"tg://user?id={message.from_user.id}"
        user = f"👤 {user_info['name']}\n" \
               f"📞 {user_info['phone']}\n"
        text += user + '💳/💵:' + payment_type + '\n'
        money = " so'm" if language == 'uz' else ' сум'
        for i in shop[0]['items']:
            text += f"{i['quantity']} ✖️ {i['product']}\n"
        text += ("🍟 Товары:" if language == 'ru' else " 🍟Mahsulotlar:") + str(shop[0]['all_shop']) + money + "\n"
        text += ("🚙 Доставка:" if language == 'ru' else "🚙 Yetkazib berish:") + str(17000) + money + "\n"
        text += ("💰 Итого:" if language == 'ru' else "💰 Jami:") + str(shop[0]['all_shop'] + 17000) + money + "\n"
        text += f"📍" + address(message.from_user.id) if address(telegram_id=message.from_user.id) else "📍 None"
        await bot.send_message(chat_id=ADMINS[0], text=text,
                               reply_markup=check_button(telegram_id=message.from_user.id,
                                                          language=language))
    else:
        await message.answer("Malumot topilmadi!")
    try:
        delete_basket(telegram_id=message.from_user.id)
    except:
        pass
