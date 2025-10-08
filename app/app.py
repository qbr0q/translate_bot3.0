import os
import telebot
from dotenv import load_dotenv


from app.database import init_db
from app.handlers import register_handlers
from app.cache.cache import init_cache


def get_token():
    load_dotenv("config.env")
    api_token = os.getenv('TOKEN')
    return api_token


def create_bot():
    api_token = get_token()
    bot = telebot.TeleBot(api_token)
    return bot


def init_app(bot):
    init_db()
    init_cache()
    register_handlers(bot)
