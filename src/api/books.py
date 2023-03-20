from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.db.session import get_db
from src.api.schemas.books import CreateBook, UpdateBook
from src.services import books as services

router = APIRouter(tags=["Books"])


@router.get("/books", status_code=200)
def list_books(db: Session = Depends(get_db)):
    try:
        services.list_books(db)
    except Exception as e:
        print(e)


@router.get("/books/{book_id}", status_code=200)
def get_book_by_id(book_id: int, db: Session = Depends(get_db)):
    try:
        services.get_book_by_id(book_id, db)
    except Exception as e:
        print(e)


@router.post("/books", status_code=201)
def create_book(payload: CreateBook, db: Session = Depends(get_db)):
    try:
        services.create_book(payload, db)
    except Exception as e:
        print(e)


@router.put("/books/{book_id}", status_code=200)
def update_book(book_id: int, payload: UpdateBook, db: Session = Depends(get_db)):
    try:
        services.update_book(book_id, payload, db)
    except Exception as e:
        print(e)


@router.delete("/books/{book_id}", status_code=200)
def remove_book(book_id: int, db: Session = Depends(get_db)):
    try:
        services.remove_book(book_id, db)
    except Exception as e:
        print(e)
