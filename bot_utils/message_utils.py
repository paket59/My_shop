def text_for_caption(name, description, base_prise):
    '''описание товара'''
    text = (
        f'<b>{name}</b>\n'
        f'<b>Описание: {description}</b>\n'
        f'<b>Цена: {float(base_prise)}</b>\n'
    )
    return text