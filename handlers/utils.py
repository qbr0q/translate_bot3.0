from telebot import types
from random import choice

from cache import Cache
from database.models import Users
from database import Session
from database.utils import insert_record


def skip(bot, message):
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


def check_word(word):
    ru_words = [i.word for i in Cache.ru_words]
    it_words = [i.word for i in Cache.it_words]

    return word in ru_words or word in it_words
