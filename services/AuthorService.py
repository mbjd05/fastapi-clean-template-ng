from typing import List, Optional

from fastapi import Depends, HTTPException
from models.AuthorModel import Author
from models.BookModel import Book

from repositories.AuthorRepository import AuthorRepository
from schemas.pydantic.AuthorSchema import AuthorSchema


class AuthorService:
    authorRepository: AuthorRepository

    def __init__(self, authorRepository: AuthorRepository = Depends()) -> None:
        self.authorRepository = authorRepository

    def create(self, author_body: AuthorSchema) -> Author:
        return self.authorRepository.create(
            Author(name=author_body.name)
        )

    def delete(self, author_id: int) -> None:
        author = self.get_author_or_404(author_id)
        self.authorRepository.delete(author)

    def get(self, author_id: int) -> Author:
        return self.get_author_or_404(author_id)

    def list(
        self,
        name: Optional[str] = None,
        pageSize: Optional[int] = 100,
        startIndex: Optional[int] = 0,
    ) -> List[Author]:
        return self.authorRepository.list(name, pageSize, startIndex)

    def update(self, author_id: int, author_body: AuthorSchema) -> Author:
        author = self.get_author_or_404(author_id)
        return self.authorRepository.update(
            author_id, Author(name=author_body.name)
        )

    def get_books(self, author_id: int) -> List[Book]:
        author = self.get_author_or_404(author_id)
        return author.books

    def get_author_or_404(self, author_id: int) -> Author:
        author = self.authorRepository.get(Author(id=author_id))
        if author is None:
            raise HTTPException(status_code=404, detail="Author not found")
        return author