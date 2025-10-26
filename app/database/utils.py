from sqlalchemy import select
from sqlalchemy.orm import joinedload

from app.database import Session
from app.database.models import User


def init_user(session, user_id):
    user = session.scalar(
        select(User).where(User.telegram_id == user_id)
    )
    if user is None:
        user = User(telegram_id=user_id)
        commit_record(user)
    return user


def commit_record(record):
    with Session() as session:
        session.add(record)
        session.commit()
        session.refresh(record)


def get_table_records(table):
    with Session() as session:
        return session.query(table).all()


def get_record(model, **filters):
    with Session() as session:
        stmt = select(model)\
            .options(joinedload("*"))\
            .filter_by(**filters)
        return session.execute(stmt).scalar()


def get_records(model, **filters):
    with Session() as session:
        stmt = select(model)\
            .options(joinedload("*"))\
            .filter_by(**filters)
        result_data = session.execute(stmt)
        return result_data.unique().scalars().all()
