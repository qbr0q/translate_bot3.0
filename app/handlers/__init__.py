from .commands import register_command_handlers
from .callbacks import register_callback_handlers
from .messages import register_message_handlers


def register_handlers(bot):
    register_command_handlers(bot)
    register_callback_handlers(bot)
    register_message_handlers(bot)
