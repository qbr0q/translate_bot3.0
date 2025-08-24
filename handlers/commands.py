from telebot import types

from cache import Cache
from cache.cache import load_cache
from .utils import skip


def register_command_handlers(bot):
    @bot.message_handler(commands=['start'])
    @load_cache
    def start(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        for arg in ('RU -> IT', 'Магазин', 'Профиль', 'Инвентарь', 'IT -> RU'):
            markup.add(
                types.KeyboardButton(arg)
            )
        bot.send_message(message.chat.id, 'Выберите язык для перевода', reply_markup=markup)

    @bot.message_handler(commands=['next'])
    @load_cache
    def skip_handler(message):
        skip(bot, message)
