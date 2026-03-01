from app.database import Session
from app.database.utils import get_record, commit_record
from app.database.models import Item, UserItem
from app.handlers.utils import is_enough_balance, add_item, reduce_balance
from app.handlers.utils import skip

from math import ceil
from sqlmodel import select


def take_amount(callback, user_id):
    stmt = select(UserItem).join(Item).where(Item.callback == callback, UserItem.user_id == user_id)
    with Session() as session:
        item = session.execute(stmt).scalar()
    item.amount -= 1
    commit_record(item)


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
    word = user.translate
    word_length = len(word)

    visible_count = ceil(word_length / 2)
    censor_count = word_length - visible_count

    visible_part = word[:visible_count]
    censored_part = '*' * censor_count
    censored_word = visible_part + censored_part

    take_amount(call.data, user.id)

    bot.send_message(call.message.chat.id, f'Половина слова - {censored_word}')


callback_dict = {
    'translated-word': translate_callback,
    'half': half_callback
}
