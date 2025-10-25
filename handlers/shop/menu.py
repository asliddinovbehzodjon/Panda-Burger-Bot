from aiogram import types,F
from loader import dp,bot
from aiogram.fsm.context import FSMContext
from keyboards.default.buttons import *
from keyboards.inline.buttons import *
from api import *
from aiogram.types.input_media_photo import InputMediaPhoto
@dp.message(F.text.in_(["❌ Отменить", "❌ Bekor qilish"]))
async def cancelfunction(message:types.Message):
    user = get_user(telegram_id=message.from_user.id)
    if user != 'Not Found':
        language = user.get('language', 'uz')
    else:
        language = 'uz'
    if language =="uz":
        await message.answer("✅ Bosh menyuga xush kelibsiz!\n" \
                             f"🍕 Mazali pitsalar! Buyurtma berishni boshlaysizmi?", reply_markup=main_button(language))
    else:
        await message.answer(f"✅ Добро пожаловать в главное меню!\n" \
                             f"🍕 Вкусные пиццы! Вы начинаете заказывать?", reply_markup=main_button(language))
######## Sub Category Products #########
@dp.message(F.text.startswith('🍽'))
async def subcategory_products(message:types.Message,state:FSMContext):
    await state.update_data({
        "level": "subcategory"
    })
    user = get_user(telegram_id=message.from_user.id)
    if user != 'Not Found':
        language = user.get('language', 'uz')
    else:
        language = 'uz'
    key = message.text[1:]
    datas = subcategory_info(subcategory=key,language=language)
    if datas.get('products',[]) ==[]:
        if language == 'uz':
            await message.answer("<b>Bu kategoriya bo'yicha mahsulot yo'q yoki yangilanmoqda!</b>")
        else:
            await message.answer("<b>В этой категории нет товаров или они обновляются!</b>")
    else:
        data = datas['products'][0]
        money = "so'm" if language == 'uz' else 'сум'
        sena = "💰 Narxi" if language == 'uz' else "💰 Цена"
        button = ReplyKeyboardBuilder()
        if language == 'uz':
            button.row(KeyboardButton(text="⬅️ Orqaga"), KeyboardButton(text="📥 Savat"))
        if language == 'ru':
            button.row(KeyboardButton(text="⬅️ Назад"), KeyboardButton(text="📥 Корзина"))
        button.adjust(2)
        await message.answer("⬇️", reply_markup=button.as_markup(resize_keyboard=True))
        photo = types.input_file.URLInputFile(url=data['image'])
        await message.answer_photo(photo=photo,
                                   caption=f"<b>{data['name']}</b>\n\n{sena} : {data['price']} {money}",
                                   reply_markup=product_button(data=datas['products'], language=language
                                                               ))
############### Function For Back Button ##############
@dp.message(F.text.startswith("⬅️"))
async def test(message:types.Message,state:FSMContext):
    data = await state.get_data()
    level = data.get('level',None)
    user = get_user(telegram_id=message.from_user.id)
    if user != 'Not Found':
        language = user.get('language', 'uz')
    else:
        language = 'uz'
    if level=='subcategory':
        if language == 'uz':
            await message.answer("⬇️ Kategoriyani tanlang", reply_markup=categories(language))
        else:
            await message.answer("⬇️ Выберите категорию", reply_markup=categories(language))
    if level=="category":
        if language == "uz":
            await message.answer("✅ Bosh menyuga xush kelibsiz!\n" \
                                 f"🍕 Mazali pitsalar! Buyurtma berishni boshlaysizmi?", reply_markup=main_button(language))
        else:
            await message.answer(f"✅ Добро пожаловать в главное меню!\n"   
                                 f"🍕 Вкусные пиццы! Вы начинаете заказывать?", reply_markup=main_button(language))
    elif level=='product-category':
        await state.update_data({
            "level": "category"
        })
        if language == 'uz':
            await message.answer("⬇️ Kategoriyani tanlang", reply_markup=categories(language))
        else:
            await message.answer("⬇️ Выберите категорию", reply_markup=categories(language))
    else:
        if language == "uz":
            await message.answer("✅ Bosh menyuga xush kelibsiz!\n"
                                 f"🍕 Mazali pitsalar! Buyurtma berishni boshlaysizmi?", reply_markup=main_button(language))
        else:
            await message.answer(f"✅ Добро пожаловать в главное меню!\n"
                                 f"🍕 Вкусные пиццы! Вы начинаете заказывать?", reply_markup=main_button(language))


############## Go to Menus ###############
@dp.message(F.text.in_(["🍴 Меню","🍴 Menyu"]))
async def category(message:types.Message,state:FSMContext):
      await state.update_data({
          "level":"category"
      })
      user = get_user(telegram_id=message.from_user.id)
      if user != 'Not Found':
          language = user.get('language', 'uz')
      else:
          language = 'uz'
      if language =='uz':
          await message.answer("⬇️ Kategoriyani tanlang",reply_markup=categories(language))
      else:
          await message.answer("⬇️ Выберите категорию", reply_markup=categories(language))
########### Go to Categories' product or Subcategory ########################
@dp.message(F.text.startswith('🍜'))
async def test(message:types.Message,state:FSMContext):
    user = get_user(telegram_id=message.from_user.id)
    if user != 'Not Found':
        language = user.get('language', 'uz')
    else:
        language = 'uz'
    key = message.text
    key = str(key[1:])
    key = key.strip()
    category = category_info(category=key.strip(),language=language)
    if category.get('subcategory',[]) !=[] and category.get('products',[]) != []:
        if language == 'uz':
            await message.answer("<b>Bu kategoriya bo'yicha mahsulot yo'q yoki yangilanmoqda!</b>")
        else:
            await message.answer("<b>В этой категории нет товаров или они обновляются!</b>")

    elif category.get('subcategory',[]) !=[]:
        await message.answer("⬇️",reply_markup=subcategory_button(language=language,subcategory=category.get('subcategory',[])))
    else:
        await state.update_data({
            "level": "product-category"
        })
        if category.get('products',None) is None:
            if language=='uz':
                await message.answer("<b>Bu kategoriya bo'yicha mahsulot yo'q yoki yangilanmoqda!</b>")
            else:
                await message.answer("<b>В этой категории нет товаров или они обновляются!</b>")
        else:
            data = category['products'][0]
            money = "so'm" if language == 'uz' else 'сум'
            sena = "💰 Narxi" if language == 'uz' else "💰 Цена"
            button = ReplyKeyboardBuilder()
            if language == 'uz':
                button.row(KeyboardButton(text="⬅️ Orqaga"), KeyboardButton(text="📥 Savat"),
                           width=2)
            if language == 'ru':
                button.row(KeyboardButton(text="⬅️ Назад"), KeyboardButton(text="📥 Корзина"),
                           width=2)
            await message.answer("⬇️", reply_markup=button.as_markup(resize_keyboard=True))
            url=types.input_file.URLInputFile(url=data['image'])

            await message.answer_photo(photo=url,
                                       caption=f"<b>{data['name']}</b>\n\n{sena} : {data['price']} {money}",
                                       reply_markup=product_button(data=category.get('products',[]),language=language))
############## Show Product (Inline Button) ##################
@dp.callback_query(ProductCallback.filter())
async def decrease(call:types.CallbackQuery,callback_data:ProductCallback,state:FSMContext):
    data =callback_data
    user = get_user(telegram_id=call.from_user.id)
    if user != 'Not Found':
        language = user.get('language', 'uz')
    else:
        language = 'uz'
    if data.action =='next':
        money = "so'm" if language == 'uz' else 'сум'
        sena = "💰 Narxi" if language == 'uz' else "💰 Цена"
        product = get_product(language=language,id=int(data.product))
        file = types.input_file.URLInputFile(url=product['image'])
        await call.message.edit_media(media=InputMediaPhoto(media=file,caption=f"<b>{product['name']}</b>\n\n"                                                                                 f"{sena}: {product['price']} {money}"),reply_markup=to_product(language=language,product=product['id'],count=1))
    if data.action =='increase':
        if language =='uz':
          await call.answer(f"{int(data.count)+1} ta")
          count = int(data.count)+1
          await call.message.edit_reply_markup(reply_markup=to_product(language=language,product=int(data.product),count=count))
        else:
            await call.answer(f"{int(data.count) + 1} шт")
            count = int(data.count) + 1
            await call.message.edit_reply_markup(
                reply_markup=to_product(language=language, product=int(data.product), count=count))
    if data.action == 'decrease':
        if language == 'uz':
            if int(data.count)==1:
                await call.answer(f"{int(data.count)} ta")
                # count = int(data['count'])
                # await call.message.edit_reply_markup(
                #     reply_markup=to_product(language=language, product=int(data['product']), count=count))
            else:
                count = int(data.count) - 1
                await call.answer(f"{int(data.count) - 1} ta")
                await call.message.edit_reply_markup(
                    reply_markup=to_product(language=language, product=int(data.product), count=count))
        else:
            if int(data.count)==1:
                await call.answer(f"{int(data.count)} шт")
                # count = int(data['count'])
                # await call.message.edit_reply_markup(
                #     reply_markup=to_product(language=language, product=int(data['product']), count=count))
            else:
                await call.answer(f"{int(data.count) - 1} шт")
                count = int(data.count) - 1
                await call.message.edit_reply_markup(
                    reply_markup=to_product(language=language, product=int(data.count), count=count))
    if data.action =='add':
        telegram_id = call.from_user.id
        quantity = int(data.count)
        product = int(data.product)
        await call.message.delete()
        set_order(telegram_id=telegram_id,product=product,quantity=quantity)
        await state.update_data({
            "level": "category"
        })
        if language == 'uz':
            await call.message.answer("<i>Mahsulot savatingizga qo'shildi.</i>")
            await call.message.answer("⬇️ Kategoriyani tanlang", reply_markup=categories(language))
        else:
            await call.message.answer('<i>Товар добавлен в вашу корзину.</i>')
            await call.message.answer("⬇️ Выберите категорию", reply_markup=categories(language))