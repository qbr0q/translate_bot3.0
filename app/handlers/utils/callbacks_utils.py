from app.database.utils import get_record
from app.database.models import Item
from app.handlers.utils import is_enough_balance, add_item, reduce_balance
from .utils import skip


def shop_callback(call, bot, user):
    item = get_record(Item, callback=call.data)
    if not is_enough_balance(user, item.price):
        bot.send_message(call.message.chat.id, 'Не хватает крабсов :(')
    else:
        add_item(user, item)
        reduce_balance(user, item)
        bot.send_message(call.message.chat.id, f'Предмет "{item.name}" успешно приобретен')


def translate_callback(call, bot, user):
    bot.send_message(call.message.chat.id, f'Перевод слова - {user.translate}')
    skip(bot, call.message, user)


def half_callback(call, bot, user):
    pass
