from aiogram.utils.keyboard import ReplyKeyboardBuilder,KeyboardButton
from api import *
def admin_button():
    button = ReplyKeyboardBuilder()
    button.row(
        KeyboardButton(text="🗣 Reklama yuborish"),
        KeyboardButton(text="📊 Obunachilar soni"),

    )
    button.adjust(2,2)
    return button.as_markup(resize_keyboard=True,one_time_keyboard=True,input_field_placeholder="Kerakli bo'limni tanlang!")
def add_type():
    button = ReplyKeyboardBuilder()
    button.row(
        KeyboardButton(text="📝 Tekst"),
        KeyboardButton(text="📸 Rasm")
    )
    button.row(
        KeyboardButton(text="🎞 Video"),
        KeyboardButton(text="⬅️ Orqaga")
    )
    button.adjust(2)
    return button.as_markup(resize_keyboard=True, one_time_keyboard=True)
def back_button():
    button = ReplyKeyboardBuilder()

    button.row(

        KeyboardButton(text="◀️ Orqaga")
    )
    button.adjust(2)
    return button.as_markup(resize_keyboard=True, one_time_keyboard=True)
def need_or_not():
    button = ReplyKeyboardBuilder()

    button.row(
        KeyboardButton(text="⏺ Bekor qilish"),
        KeyboardButton(text="🆗 Kerakmas")
    )
    button.adjust(2)
    return button.as_markup(resize_keyboard=True, one_time_keyboard=True)
def send():
    button = ReplyKeyboardBuilder()

    button.row(
        KeyboardButton(text="⏺ Bekor qilish"),
        KeyboardButton(text="📤 Yuborish")
    )
    button.adjust(2)
    return button.as_markup(resize_keyboard=True, one_time_keyboard=True)
# Language
def language_button():
    btn = ReplyKeyboardBuilder()
    btn.button(text="🇺🇿 O'zbek tili")
    btn.button(text="🇷🇺 Pусский язык")
    btn.adjust(2)
    return btn.as_markup(resize_keyboard=True)
# Main Page
def main_button(language:str='uz'):
    main = ReplyKeyboardBuilder()
    if language=='uz':
        main.button(text="🍴 Menyu")
        main.button(text="🛍 Buyurtmalarim")
        main.button(text="📥 Savat")
        main.button(text="✍️ Sharh qoldiring")
        main.button(text="⚙️ Sozlamalar")
    else:
        main.button(text="🍴 Меню")
        main.button(text="🛍 Мои заказы")
        main.button(text="📥 Корзина")
        main.button(text="✍️ Оставить отзыв")
        main.button(text="⚙️ Настройки")
    main.adjust(2)
    return main.as_markup(resize_keyboard=True)
def settings(language):
    btn= ReplyKeyboardBuilder()
    btn.button(text="🇺🇿 O'zbek tili")
    btn.button(text="🇷🇺 Pусский язык")
    if language=='uz':
        btn.button(text="🔝 Bosh menyuga qaytish")
    else:
        btn.button(text="🔝 Вернуться в главное меню")
    btn.adjust(2)
    return btn.as_markup(resize_keyboard=True)
def cancel(language):
    button = ReplyKeyboardBuilder()
    if language=='ru':
        button.button(text="❌ Отменить")
    else:
        button.button(text="❌ Bekor qilish")
    button.adjust(1)
    return button.as_markup(resize_keyboard=True)
def categories(language):
    button = ReplyKeyboardBuilder()
    if language=='uz':
        button.row(KeyboardButton(text="⬅️ Orqaga"),KeyboardButton(text="📥 Savat"),
                   width=2)
    if language =='ru':
        button.row(KeyboardButton(text="⬅️ Назад"), KeyboardButton(text="📥 Корзина"))
    datas = get_categories(language)
    for data in datas:
        button.button(text=f"🍜{data}")
    button.adjust(2)

    return button.as_markup(resize_keyboard=True)
def get_contact(language):
    button = ReplyKeyboardBuilder()
    if language == 'uz':
        button.row(KeyboardButton(text="📞 Telefon raqamimni jo'natish",request_contact=True),
                   KeyboardButton(text="❌ Bekor qilish"),
                   width=2)
    else:
        button.row(KeyboardButton(text="📞 Поделитесь моим номером телефона",request_contact=True),
                   KeyboardButton(text="❌ Отменить"),
                   width=2)

    return button.as_markup(resize_keyboard=True)
def get_location(language):
    button = ReplyKeyboardBuilder()
    if language == 'uz':
        button.row(KeyboardButton(text="📍 Manzilni yuborish", request_location=True),
                   KeyboardButton(text="❌ Bekor qilish"),
                   width=2)
    else:
        button.row(KeyboardButton(text="📍 Адрес доставки", request_location=True),
       KeyboardButton(text="❌ Отменить"),
                   width=2)
    return button.as_markup(resize_keyboard=True)
def payment_button(language):
    btn  = ReplyKeyboardBuilder()
    if language=='uz':
        btn.button(text="Naqd")
        btn.button(text="Click")
        btn.row(KeyboardButton(text="⬅️ Orqaga"), KeyboardButton(text="❌ Bekor qilish"),
                   width=2)
    else:
        btn.button(text="Наличные")
        btn.button(text="Click")
        btn.row(KeyboardButton(text="⬅️ Назад"), KeyboardButton(text="❌ Отменить"),
                   width=2)
    return btn.as_markup(resize_keyboard=True)
def gettype(language):
    button = ReplyKeyboardBuilder()
    if language == 'uz':
        button.button(text="🏃 Olib ketish")
        button.button(text="🚕 Yetkazish")
        button.button(text="❌ Bekor qilish")
    else:
        button.button(text="🏃 С собой")
        button.button(text="🚕 Доставка")
        button.button(text="❌ Отменить")
    button.adjust(1)
    return button.as_markup(resize_keyboard=True)
