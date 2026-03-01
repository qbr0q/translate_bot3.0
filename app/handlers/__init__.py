from app.handlers.command.commands import register_command_handlers
from app.handlers.callback.callbacks import register_callback_handlers
from app.handlers.message.messages import register_message_handlers


def register_handlers(bot):
    register_command_handlers(bot)
    register_callback_handlers(bot)
    register_message_handlers(bot)
