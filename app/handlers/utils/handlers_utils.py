from telebot import types

from app.handlers.utils import skip, check_word
from app.database.utils import get_records, get_table_records
from app.database.models import UserItem, Item


def to_it_handler(message, bot, user):
    user.language = 'IT'
    bot.send_message(message.chat.id, 'Язык успешно установлен: бот будет отправлять слова на итальянском')
    skip(bot, message, user)


def to_ru_handler(message, bot, user):
    user.language = 'RU'
    bot.send_message(message.chat.id, 'Язык успешно установлен: бот будет отправлять слова на русском')
    skip(bot, message, user)


def shop_handler(message, bot, user):
    shop_items = get_table_records(Item)
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


def inventory_handler(message, bot, user):
    markup = types.InlineKeyboardMarkup()
    user_items = get_records(UserItem, user_id=user.id)

    for user_item in user_items:
        markup.add(types.InlineKeyboardButton(
            f'{user_item.item.name} | {user_item.amount} шт.',
            callback_data=user_item.item.callback
        ))

    bot.send_message(
        message.chat.id, '--- Инвентарь ---', reply_markup=markup
    )
