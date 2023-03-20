class BookNotFound(Exception):
    def __init__(self, book_id: int) -> None:
        super().__init__(f"Book {book_id} not found")
