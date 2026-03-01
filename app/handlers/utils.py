from telebot import types
from random import choice

from app.cache import Cache
from app.database.utils import commit_record, get_record
from app.database.models import UserItem


def skip(bot, message, user):
    lan = Cache.user.language
    word_obj = None

    if lan == 'RU':
        word_obj = choice(Cache.ru_words_objects)
    elif lan == 'IT':
        word_obj = choice(Cache.it_words_objects)
    user.translate = word_obj.translate

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(
        'Показать перевод', callback_data='translated-word'
    ))

    bot.send_message(message.chat.id, f'Слово для перевода - {word_obj.word}', reply_markup=markup)


def check_word(word):
    return word in Cache.ru_words_list or word in Cache.it_words_list


def is_enough_balance(user, price):
    return user.balance >= price


def add_item(user, item):
    record = get_record(UserItem, item=item, user=user)
    if not record:
        record = UserItem(item_id=item.id, user_id=user.id)
    else:
        record.amount += 1
    commit_record(record)


def reduce_balance(user, item):
    user.balance -= item.price
