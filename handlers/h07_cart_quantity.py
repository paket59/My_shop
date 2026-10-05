from aiogram import Router, F, Bot
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import CallbackQuery, FSInputFile

from database.utils import db_get_product_by_name

router = Router()

@router.callback_query(F.data.regexp(r'action [+-]'))
async def change_product_quantity(callback: CallbackQuery, bot: Bot):
    """меняем количество продуктов"""
    chat_id = callback.message.chat.id
    message_id = callback.message.message_id
    action = callback.data.split()[-1]

    product_name = callback.message.caption.split('\n')[0]
    product = db_get_product_by_name()