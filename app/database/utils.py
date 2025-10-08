from sqlalchemy import select

from app.database import Session
from app.database.models import User


def init_user(session, user_id):
    user = session.scalar(
        select(User).where(User.telegram_id == user_id)
    )
    if user is None:
        user = User(telegram_id=user_id)
        insert_record(session, user)
    return user


def insert_record(session, record):
    session.add(record)
    session.commit()
    session.refresh(record)


def get_records(table):
    with Session() as session:
        return session.query(table).all()
