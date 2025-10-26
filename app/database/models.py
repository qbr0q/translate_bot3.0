from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship


class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    telegram_id: int
    balance: int = Field(default=10)
    language: str = Field(nullable=True, default='RU')
    translate: str = Field(nullable=True)
    is_check_mode: bool = Field(nullable=True, default=False)

    items: List["UserItem"] = Relationship(back_populates="user")


class RussianWord(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    word: str
    translate: str


class ItalianWord(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    word: str
    translate: str


class Item(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    price: int
    callback: str

    user_items: List["UserItem"] = Relationship(back_populates="item")


class UserItem(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    item_id: str = Field(foreign_key='item.id')
    amount: int = Field(nullable=True, default=1)
    user_id: int = Field(foreign_key='user.id')

    user: Optional[User] = Relationship(back_populates="items")
    item: Optional[Item] = Relationship(back_populates="user_items")
