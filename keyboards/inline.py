from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from database.utils import db_get_all_category, db_get_finally_price, db_get_products


def create_category_menu(chat_id):
    """Предоставление меню с категориями товаров"""
    categories = db_get_all_category()
    total_price = db_get_finally_price(chat_id)

    builder = InlineKeyboardBuilder()
    builder.button(text= f'корзина заказа ({total_price if total_price else 0}₽)',
                   callback_data='корзин азаказа'
                  )
    [builder.button(text=category.category_name, callback_data= f'category_{category.id}') for category in categories]

    builder.adjust(2, 1)
    return builder.as_markup()

def show_product_by_category(category_id):
    '''Демонстрация товаров по категориям'''
    product = db_get_products(category_id)
    builder = InlineKeyboardBuilder()
    [builder.button(text=product.product_name, callback_data = f'product_view_{product.id}') for product in product]
    builder.adjust(3)
    builder.row(InlineKeyboardButton(text='◀ Назад', callback_data='from_detail_to_category'))
    return builder.as_markup(resize_keyboard=True)