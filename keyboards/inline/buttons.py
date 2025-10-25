from aiogram.utils.keyboard import InlineKeyboardBuilder,ReplyKeyboardBuilder
from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton,KeyboardButton
from api import *
class ProductCallback(CallbackData,prefix='callback'):
    action:str
    count:int
    product:int
class CommentCallback(CallbackData,prefix='comment'):
    telegram_id:str
    language:str
class BasketCallback(CallbackData,prefix='basket'):
    action:str
    product:int
class CheckCallback(CallbackData,prefix='check'):
    telegram_id:str
    status:str
    language:str

class Format(CallbackData,prefix='ikb0000'):
    choose:str
def text_format(choose=None):
    choose = 'TEXT' if choose==None else choose
    btn  = InlineKeyboardBuilder()
    btn.button(text=f"Markup format: {choose}",callback_data=Format(choose=choose))
    return btn.as_markup()
# Products Button
def product_button(data,language):
    button = InlineKeyboardBuilder()
    product = data[0]['id']
    if len(data) > 1:
        for i in data[1:]:
            button.button(text=f"{i['name']} {i['price']}",
                                            callback_data=ProductCallback(action="next", product=i['id'], count=1).pack())
    button.row(InlineKeyboardButton(text="-", callback_data=ProductCallback(action="decrease", count=1, product=product).pack()),
               InlineKeyboardButton(text="1", callback_data="1"),
               InlineKeyboardButton(text="+", callback_data=ProductCallback(action="increase", count=1, product=product).pack()),
               width=3)
    if language == 'ru':
        button.row(InlineKeyboardButton(text="📥 Добавить в корзину",
                                        callback_data=ProductCallback(action="add", count=1, product=product).pack()))
    else:
        button.row(InlineKeyboardButton(text="📥 Savatga qo'shish",
                                        callback_data=ProductCallback(action="add", count=1, product=product).pack()))
    return button.as_markup()
def subcategory_button(language,subcategory):
    button = ReplyKeyboardBuilder()
    for data in subcategory:
        button.button(text=f"🍽 {data['name']}")
    button.adjust(2)
    if language == 'uz':
        button.row(KeyboardButton(text="⬅️ Orqaga"), KeyboardButton(text="📥 Savat"),
                   width=2)
    if language == 'ru':
        button.row(KeyboardButton(text="⬅️ Назад"), KeyboardButton(text="📥 Корзина"),
                   width=2)
    return button.as_markup(resize_keyboard=True)
# Product Or Subcategory
def product_or_subcategory(category,language,product=None):
    data = category_info(category=category)
    if data.get('subcategory',[]) !=[]:
        button = ReplyKeyboardBuilder()
        if language == 'uz':
            button.row(KeyboardButton(text="⬅️ Orqaga"), KeyboardButton(text="📥 Savat"),
                       width=2)
        if language == 'ru':
            button.row(KeyboardButton(text="⬅️ Назад"), KeyboardButton(text="📥 Корзина"),
                       width=2)
        datas = data['subcategory']
        for data in datas:
            button.button(text=f"🍽 {data}")
        button.adjust(2)
        return button.as_markup(resize_keyboard=True)
    else:
        button  = InlineKeyboardBuilder()
        data = data.get('products',[])
        if data != []:
            for i in data[1:]:
                button.button(text=f"{i['name']} {i['price']}",
                              callback_data=ProductCallback(action="next", product=i['id'], count=1).pack())
        button.row(InlineKeyboardButton(text="-", callback_data=ProductCallback(action="decrease", count=1,
                                                                                product=product).pack()),
                   InlineKeyboardButton(text="1", callback_data="1"),
                   InlineKeyboardButton(text="+", callback_data=ProductCallback(action="increase", count=1,
                                                                                product=product).pack()),
                   width=3)
        if language == 'ru':
            button.row(InlineKeyboardButton(text="📥 Добавить в корзину",
                                        callback_data=ProductCallback(action="add", count=1, product=product).pack()))
        else:
             button.row(InlineKeyboardButton(text="📥 Savatga qo'shish",
                                        callback_data=ProductCallback(action="add", count=1, product=product).pack()))
        return button.as_markup()
# Product
def to_product(language,product,count:int):
    button = InlineKeyboardBuilder()
    button.row(InlineKeyboardButton(text="-", callback_data=ProductCallback(action="decrease", count=count, product=product).pack()),
               InlineKeyboardButton(text=f"{count}", callback_data=str(count)),
               InlineKeyboardButton(text="+", callback_data=ProductCallback(action="increase", count=count, product=product).pack()))
    if language == 'ru':
        button.row(InlineKeyboardButton(text="📥 Добавить в корзину",
                                        callback_data=ProductCallback(action="add", count=count, product=product).pack()))
    else:
        button.row(InlineKeyboardButton(text="📥 Savatga qo'shish",
                                        callback_data=ProductCallback(action="add", count=count, product=product).pack()))
    return button.as_markup()
def basket_button(language,datas):
    button  = InlineKeyboardBuilder()
    if language=='uz':
        button.row(InlineKeyboardButton(text="🗑 Savatni tozalash",callback_data=BasketCallback(action='clear',product=0).pack()),InlineKeyboardButton(text="🚖 Buyurtma berish",callback_data=BasketCallback(action='order',product=0).pack()),
                   width=2)
    else:
        button.row(InlineKeyboardButton(text="🗑 Очистить корзину",
                                        callback_data=BasketCallback(action='clear', product=0).pack()),
                   InlineKeyboardButton(text="🚖 Оформить заказ",
                                        callback_data=BasketCallback(action='order', product=0).pack()),
                   width=2)

    for data in datas:
        button.button(text=f"❌ {data['product']}",callback_data=BasketCallback(action='delete',product=data['product_id']).pack())
    button.adjust(1)
    return button.as_markup()
def check_button(telegram_id,language):
    button = InlineKeyboardBuilder()
    telegram_id = str(telegram_id)
    if language == 'uz':
        button.button(text="✅ Qabul qilindi",callback_data=CheckCallback(telegram_id=telegram_id,status='ok',language=language).pack())
        button.button(text="❌ Bekor qilish",callback_data=CheckCallback(
           telegram_id=telegram_id, status='bad', language=language
        ).pack())
    else:
        button.button(text="✅ Получено",
                                        callback_data=CheckCallback(telegram_id=telegram_id, status='ok',
                                                                         language=language).pack())
        button.button(text="❌ Bekor qilish", callback_data=CheckCallback(
            telegram_id=telegram_id, status='bad', language=language
        ).pack())
    button.adjust(1)
    return button.as_markup()
def comment_button(telegram_id,language):
    btn = InlineKeyboardBuilder()
    telegram_id = str(telegram_id)
    btn.button(text="Profile",url=f'tg://user?id={telegram_id}')
    btn.button(text="Qisqa javob" if language=='uz' else "Короткий ответ",callback_data=CommentCallback(telegram_id=telegram_id,language=language).pack())
    btn.adjust(1)
    return btn.as_markup()