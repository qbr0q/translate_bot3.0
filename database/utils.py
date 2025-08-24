from sqlalchemy import select

from database.models import Users


def init_user(session, user_id):
    user = session.scalar(
        select(Users).where(Users.telegram_id == user_id)
    )
    if user is None:
        user = Users(telegram_id=user_id)
        insert_record(session, user)
    return user


def insert_record(session, record):
    session.add(record)
    session.commit()
    session.refresh(record)


def get_records(session, table):
    return session.query(table).all()
