from app.cache import load_cache
from app.handlers.utils import to_it_handler, to_ru_handler, shop_handler,\
    check_mode_handler, other_mes_handler


def register_message_handlers(bot):
    @bot.message_handler()
    @load_cache
    def messages(message, user):
        message_text = message.text

        handlers_dict = {
            'RU -> IT': to_it_handler,
            'IT -> RU': to_ru_handler,
            'Магазин': shop_handler
        }
        if user.is_check_mode:
            handler = check_mode_handler
        else:
            handler = handlers_dict.get(message_text, other_mes_handler)
        handler(message, bot, user)
