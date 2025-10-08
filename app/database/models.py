from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    telegram_id: int
    language: str = Field(nullable=True, default='RU')
    translate: str = Field(nullable=True)
    is_check_mode: bool = Field(nullable=True, default=False)


class RussianWords(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    word: str
    translate: str


class ItalianWords(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    word: str
    translate: str


class Shop(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    price: int
    callback: str
