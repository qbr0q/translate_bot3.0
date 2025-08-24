from cache import Cache
from cache.cache import load_cache


def register_message_handlers(bot):
    @bot.message_handler()
    @load_cache
    def messages(message):
        message_text = message.text
        user_id = message.chat.id

        if message_text == 'RU -> IT':
            Cache.user.language = 'RU'
            bot.send_message(user_id, 'Язык успешно установлен: бот будет отправлять слова на русском')
        elif message_text == 'IT -> RU':
            Cache.user.language = 'IT'
            bot.send_message(user_id, 'Язык успешно установлен: бот будет отправлять слова на итальянском')
