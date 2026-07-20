from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardMarkup, ReplyKeyboardBuilder


def start_keyboard():
    '''начинает работу магазина'''
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='начать 🤠')]
        ],
        resize_keyboard=True
    )

def get_main_menu():
    '''создание основного меню сервиса'''
    builder = ReplyKeyboardMarkup()
    builder.button(text='Оформить заказ 🚚')
    builder.button(text='Корзина 🛒')
    builder.button(text='История')
    builder.button(text='Настройки ⚙')
    builder.adjust(1,3)
    return builder.as_markup(resize_keyboard=True)