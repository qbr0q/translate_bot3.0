import json

from cache import Cache
from database import Session
from database.models import RussianWords, ItalianWords
from database.utils import get_records


def init_cache():
    ru_words = get_records(RussianWords)
    it_words = get_records(ItalianWords)

    Cache.ru_words = ru_words
    Cache.it_words = it_words


def load_cache(func):
    def wrapper(message):
        with Session() as session:
            Cache.get_or_load(message.from_user.id, session)
            func(message)
        Cache.save()
    return wrapper
