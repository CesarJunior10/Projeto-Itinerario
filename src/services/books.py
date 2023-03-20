from typing import List, Optional

from sqlalchemy.orm import Session

from src.api.schemas.books import CreateBook, UpdateBook
from src.models.book import Book
from src.exceptions import BookNotFound


def list_books(db: Session) -> List[dict]:
    books = db.execute("SELECT * FROM livros").fetchall()
    return [dict(b) for b in books]


def get_book_by_id(book_id: int, db: Session) -> dict:
    book = db.execute(
        "SELECT * FROM livros WHERE id=:id", {"id": book_id}
    ).fetchone()
    if not book:
        raise BookNotFound(book_id)
    return dict(book)


def create_book(payload: CreateBook, db: Session):
    book = Book(author=payload.author, title=payload.title)
    db.add(book)
    print(f"Creating book {book}")
    db.commit()


def update_book(book_id: int, payload: UpdateBook, db: Session):
    book: Optional[Book] = db.query(Book).filter_by(id=book_id).first()
    if not book:
        raise BookNotFound(book_id)
    book.author = payload.author
    book.title = payload.title
    print(f"Updating book {book}")
    db.commit()


def remove_book(book_id: int, db: Session):
    book: Optional[Book] = db.query(Book).filter_by(id=book_id).first()
    if not book:
        raise BookNotFound(book_id)
    db.delete(book) 
    db.commit()
