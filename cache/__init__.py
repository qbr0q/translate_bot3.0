from database import Session
from database.utils import init_user


class Cache:
    user = None
    ru_words = []
    it_words = []

    @classmethod
    def get_or_load(cls, user_id, session=None):
        if not cls.user:
            user = cls._load_user(session, user_id)
            cls.set(user)

    @classmethod
    def get(cls):
        return cls.user

    @classmethod
    def set(cls, user):
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
            print()
