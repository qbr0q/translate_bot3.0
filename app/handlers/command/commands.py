from telebot import types

from app.cache import load_cache
from app.handlers.utils import skip
from app.handlers.command.utils import MODEL_TO_COMMAND_MAP
from app.database.utils import commit_record


def register_command_handlers(bot):
    @bot.message_handler(commands=['start'])
    @load_cache
    def start(message, user):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        for arg in ('RU -> IT', 'Магазин', 'Профиль', 'Инвентарь', 'IT -> RU'):
            markup.add(
                types.KeyboardButton(arg)
            )
        bot.send_message(message.chat.id, 'Выберите язык для перевода', reply_markup=markup)

    @bot.message_handler(commands=['next'])
    @load_cache
    def skip_handler(message, user):
        skip(bot, message, user)

    @bot.message_handler(commands=['check_mode'])
    @load_cache
    def check_mode(message, user):
        if user.is_check_mode:
            user.is_check_mode = False
            bot.send_message(message.chat.id, 'Режим проверки слов выключен')
        else:
            user.is_check_mode = True
            bot.send_message(message.chat.id, 'Вы в режиме проверки слов. Чтобы выключить режим,'
                                      ' используйте /check_mode')

    @bot.message_handler(commands=['help'])
    def help_mess(message):
        mess_help = '/username - узнать или установить юзернейм (/username name)\n' \
                    '/bet - засандалить сочную ставочку (/bet ставка+цвет)\n' \
                    '/balance - узнать баланс\n' \
                    '/give - передать баланс (ответить на сообщение получателя)'
        bot.send_message(chat_id=message.chat.id, text=mess_help)


    @bot.message_handler(commands=['add_ru', 'add_it'])
    def add_ru(message):
        command, message_body = message.text.split(" ", 1)
        words = message_body.split(" - ")
        word = words[0]
        translate = words[1:]
        model = MODEL_TO_COMMAND_MAP.get(command)

        record = model(word=word, translate=", ".join(translate))
        commit_record(record)

        bot.send_message(chat_id=message.chat.id, text="Слово добавлено!")



    @bot.message_handler(func=lambda message: message.text.startswith('/'))
    def unknown_command(message):
        bot.send_message(chat_id=message.chat.id,
                         text=f"Неизвестная команда: {message.text}. "
                              f"Для помощи воспользуйтесь командой /help")
