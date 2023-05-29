from pydantic import BaseModel
from typing import Optional


class ArticleBase(BaseModel):
    title: str
    text: Optional[str]
    image: Optional[str]
    is_publish: bool = False


class ArticleCreate(ArticleBase):
    pass


class Article(ArticleBase):
    id: int

    class Config:
        orm_modde = True