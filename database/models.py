from sqlmodel import SQLModel, Field
from sqlalchemy import JSON
from typing import List


class Users(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    telegram_id: int
    language: str = Field(nullable=True, default='RU')
    translate: str = Field(nullable=True)


class RussianWords(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    word: str
    translate: str


class ItalianWords(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    word: str
    translate: str
