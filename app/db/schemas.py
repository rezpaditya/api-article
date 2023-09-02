from pydantic import BaseModel
from typing import Optional


class Article(BaseModel):
    id: int
    title: str
    text: Optional[str]
    image: Optional[str]
    is_publish: bool = False
    author_id: int

    class Config:
        orm_mode = True


class Author(BaseModel):
    id: int
    first_name: str
    last_name: str

    class Config:
        orm_mode = True
        