from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Article(BaseModel):
    title: str
    text: str
    image: str
    is_publish: bool = False


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/article/{article_id}")
def read_article(article_id: int, q: Union[str, None] = None):
    return {"article_id": article_id, "q": q}


@app.put("/articles/{article_id}")
def update_article(article_id: int, article: Article):
    return {"title": article.title, "article_id": article_id}