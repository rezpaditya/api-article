from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db import models, crud, schemas
from db.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/articles/", response_model=list[schemas.Article])
def read_articles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    articles = crud.get_articles(db, skip=skip, limit=limit)
    if articles:
        return [article.json() for article in articles]
    else:
        raise HTTPException(status_code=404, detail="failed to fetch articles...")


@app.post("/articles", response_model=schemas.Article)
def create_article(article: schemas.ArticleCreate, db: Session = Depends(get_db)):
    db_article = crud.create_article(db=db, article=article)
    if db_article:
        return db_article.json()
    else:
        raise HTTPException(status_code=401, detail="Failed to create article...")
