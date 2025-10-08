from telebot import types
from random import choice

from app.cache import Cache
from app.database.utils import get_records
from app.database.models import Shop


def skip(bot, message, user):
    lan = Cache.user.language
    word_obj = None

    if lan == 'RU':
        word_obj = choice(Cache.ru_words_objects)
    elif lan == 'IT':
        word_obj = choice(Cache.it_words_objects)
    Cache.user.translate = word_obj.translate

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(
        'Показать перевод', callback_data='translated-word'
    ))

    bot.send_message(message.chat.id, f'Слово для перевода - {word_obj.word}', reply_markup=markup)


def check_word(word):
    return word in Cache.ru_words_list or word in Cache.it_words_list


def to_it_handler(message, bot, user):
    user.language = 'IT'
    bot.send_message(message.chat.id, 'Язык успешно установлен: бот будет отправлять слова на итальянском')
    skip(bot, message, user)


def to_ru_handler(message, bot, user):
    user.language = 'RU'
    bot.send_message(message.chat.id, 'Язык успешно установлен: бот будет отправлять слова на русском')
    skip(bot, message, user)


def shop_handler(message, bot, user):
    shop_items = get_records(Shop)
    markup = types.InlineKeyboardMarkup()

    for shop_item in shop_items:
        markup.add(types.InlineKeyboardButton(
            f'{shop_item.name} | {shop_item.price} крабсов',
            callback_data=shop_item.callback
        ))

    bot.send_message(
        message.chat.id, '--- Магазин ---', reply_markup=markup
    )


def other_mes_handler(message, bot, user):
    if message.text in user.translate.split(', '):
        bot.send_message(message.chat.id, f"Правильный ответ!✔\n"
                                          f"Другие переводы слова: {user.translate}")
        skip(bot, message, user)
    else:
        bot.send_message(message.chat.id, 'Ответ неправильный')


def check_mode_handler(message, bot, user):
    responses = ('Такого слова еще нет в словаре', 'Такое слово уже есть в словаре')
    is_word_recorded = check_word(message.text)
    bot.send_message(message.chat.id, responses[is_word_recorded])


def translate_callback(call, bot, user):
    bot.send_message(call.message.chat.id, f'Перевод слова - {user.translate}')
    skip(bot, call.message, user)


def half_callback(call, bot, user):
    pass
