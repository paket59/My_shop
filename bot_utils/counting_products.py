from database.utils import db_get_cart_items


def couinting_poducts_from_cart(chat_id, user_text):
    '''Подсчитываем товары из корзины'''
    items = db_get_cart_items(chat_id)
    if not items:
        return None

    text = f'<b>{user_text}</b>\n '
    total_products = 0
    total_price = 0
    count = 0
    cart_id = None

    for idx, item in enumerate(items, start=1):
        name = item['product_name']
        qty = item['quantity']
        price = float(item['final_price'])

        item_total = price
        total_price += item_total
        total_products += qty
        count += 1
        cart_id = item['product_id']

        text += f'<b>{idx}:{name}</b>\n '
        text += f'<b>количество:{qty}</b>\n '
        text += f'<b>стоимость:{item_total:.2f}₽</b>\n '

    text += (f'<b>общее количество продуктов:{total_products}</b>\n '
    f'<b>стоимость всех товаров:{total_price:.2f}₽</b>\n ')
    return count,text,total_price,cart_id