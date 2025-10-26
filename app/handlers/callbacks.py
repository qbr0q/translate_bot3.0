from app.cache import load_cache
from app.handlers.utils.callbacks_utils import translate_callback, half_callback, \
    shop_callback


def register_callback_handlers(bot):
    @bot.callback_query_handler(func=lambda call: True)
    @load_cache
    def answer(call, user):
        callback = None
        if 'магазин' in call.message.text.lower():
            callback = shop_callback
        callback_dict = {
            'translated-word': translate_callback,
            'half': half_callback
        }
        if not callback:
            callback = callback_dict.get(call.data)
        callback(call, bot, user)
