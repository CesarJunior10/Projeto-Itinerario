from pydantic import BaseModel


class CreateBook(BaseModel):
    title: str
    author: str


class UpdateBook(CreateBook):
    pass
