from telebot import types

from cache import Cache
from cache.cache import load_cache
from .utils import skip, check_word
from database.utils import get_records
from database.models import Shop


def register_message_handlers(bot):
    @bot.message_handler()
    @load_cache
    def messages(message):
        message_text = message.text
        user_id = message.chat.id

        handlers_dict = {
            'RU -> IT': to_it_handler,
            'IT -> RU': to_ru_handler,
            'Магазин': shop_handler
        }
        if Cache.user.is_check_mode:
            handler = check_mode_handler
        else:
            handler = handlers_dict.get(message_text, other_mes_handler)
        handler(message)


    # messages handlers
    def to_it_handler(message):
        Cache.user.language = 'IT'
        bot.send_message(message.chat.id, 'Язык успешно установлен: бот будет отправлять слова на итальянском')
        skip(bot, message)

    def to_ru_handler(message):
        Cache.user.language = 'RU'
        bot.send_message(message.chat.id, 'Язык успешно установлен: бот будет отправлять слова на русском')
        skip(bot, message)

    def shop_handler(message):
        shop_items = get_records(Shop)
        markup = types.InlineKeyboardMarkup()

        for shop_item in shop_items:
            markup.add(types.InlineKeyboardButton(
                f'{shop_item.name} | {shop_item.price} крабсов',
                callback_data='1'
            ))

        bot.send_message(
            message.chat.id, '--- Магазин ---', reply_markup=markup
        )

    def other_mes_handler(message):
        if message.text in Cache.user.translate.split(', '):
            bot.send_message(message.chat.id, f"Правильный ответ!✔\n"
                                      f"Другие переводы слова: {Cache.user.translate}")
            skip(bot, message)
        else:
            bot.send_message(message.chat.id, 'Ответ неправильный')

    def check_mode_handler(message):
        responses = ('Такого слова еще нет в словаре', 'Такое слово уже есть в словаре')
        is_word_recorded = check_word(message.text)
        bot.send_message(message.chat.id, responses[is_word_recorded])
