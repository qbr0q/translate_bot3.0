from telebot import types
from random import choice

from cache import Cache
from database.models import Users
from database import Session
from database.utils import insert_record


def skip(bot, message):
    try:
        lan = Cache.user.language
    except Exception as e:
        print()
    lan = Cache.user.language
    word_obj = None

    if lan == 'RU':
        word_obj = choice(Cache.ru_words)
    elif lan == 'IT':
        word_obj = choice(Cache.it_words)
    Cache.user.translate = word_obj.translate

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(
        'Показать перевод', callback_data='translated-word'
    ))

    bot.send_message(message.chat.id, f'Слово для перевода - {word_obj.word}', reply_markup=markup)
