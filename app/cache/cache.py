from app.database import Session
from app.database.models import RussianWords, ItalianWords
from app.database.utils import get_records, init_user


class Cache:
    user = None
    ru_words_objects = []
    it_words_objects = []
    ru_words_list = []
    it_words_list = []

    @classmethod
    def get_or_load(cls, user_id, session=None):
        user = cls.get_user()
        if not user:
            user = cls._load_user(session, user_id)
            cls.set_user(user)
        return user

    @classmethod
    def get_user(cls):
        return cls.user

    @classmethod
    def set_user(cls, user):
        cls.user = user

    @classmethod
    def _load_user(cls, session, user_id):
        user = init_user(session, user_id)
        return user

    @classmethod
    def save(cls):
        with Session() as session:
            session.expire_on_commit = False
            session.add(cls.user)
            session.commit()


def init_cache():
    for lang, model in [('ru', RussianWords), ('it', ItalianWords)]:
        objs = get_records(model)
        setattr(Cache, f"{lang}_words_objects", objs)
        setattr(Cache, f"{lang}_words_list", [obj.word for obj in objs])


def load_cache(func):
    def wrapper(message):
        with Session() as session:
            user = Cache.get_or_load(message.from_user.id, session)
            func(message, user)
        Cache.save()
    return wrapper
