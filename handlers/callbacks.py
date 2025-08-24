from cache import Cache
from cache.cache import load_cache
from .commands import skip


def register_callback_handlers(bot):
    @bot.callback_query_handler(func=lambda call: True)
    @load_cache
    def answer(call):
        if call.data == 'translated-word':
            bot.send_message(call.message.chat.id, f'Перевод слова - {Cache.user.translate}')
            skip(bot, call.message)
