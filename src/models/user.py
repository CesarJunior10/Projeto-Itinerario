from typing import Any

from sqlalchemy import Column, Integer, String

from src.db.session import Base


class User(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(256), nullable=False)
    password = Column(String(256), nullable=False)

    def __init__(self, email: str, password: str) -> None:
        self.email = email
        self.password = password

    def __repr__(self) -> str:
        return f"<Book (email={self.email})"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, User):
            return False
        return self.email == other.email

    def __hash__(self) -> int:
        return hash((self.email))
