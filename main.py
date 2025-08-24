import telebot
import os
from dotenv import load_dotenv

from database import init_db
from handlers import register_handlers
from cache.cache import init_cache


load_dotenv("config.env")
TOKEN = os.getenv('TOKEN')

bot = telebot.TeleBot(TOKEN)


def main():
    init_db()
    init_cache()
    register_handlers(bot)
    bot.infinity_polling()


if __name__ == "__main__":
    main()
