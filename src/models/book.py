from typing import Any

from sqlalchemy import Column, Integer, String

from src.db.session import Base


class Book(Base):
    __tablename__ = "livros"

    id = Column(Integer, primary_key=True, autoincrement=True)
    author = Column(String(256), nullable=False)
    title = Column(String(256), nullable=False)

    def __init__(self, author: str, title: str) -> None:
        self.author = author
        self.title = title

    def __repr__(self) -> str:
        return f"<Book (author={self.author}, title={self.title})"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Book):
            return False
        return (self.author, self.title) == (other.author, other.title)

    def __hash__(self) -> int:
        return hash((self.title))
