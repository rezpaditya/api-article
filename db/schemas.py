from pydantic import BaseModel


class ArticleBase(BaseModel):
    title: str
    text: str
    image: str
    is_publish: bool = False


class ArticleCreate(ArticleBase):
    pass


class Article(ArticleBase):
    id: int

    class Config:
        orm_modde = True