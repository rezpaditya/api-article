from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import models, crud, schemas
from app.db.database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
        return articles
    else:
        raise HTTPException(status_code=404, detail="failed to fetch articles...")
    

@app.get("/articles/{article_id}", response_model=schemas.Article)
def read_articles(article_id, db: Session = Depends(get_db)):
    article = crud.get_article(db, article_id=article_id)
    if article:
        return article
    else:
        raise HTTPException(status_code=404, detail=f"Article ID {article_id} is not found...")


@app.post("/articles", response_model=schemas.Article)
def create_article(article: schemas.ArticleCreate, db: Session = Depends(get_db)):
    db_article = crud.create_article(db=db, article=article)
    if db_article:
        return db_article
    else:
        raise HTTPException(status_code=401, detail="Failed to create article...")


@app.patch("/articles", response_model=schemas.Article)
def create_article(article: schemas.Article, db: Session = Depends(get_db)):
    db_article = crud.update_article(db=db, article=article)
    if db_article:
        return db_article
    else:
        raise HTTPException(status_code=401, detail=f"Failed to update article with ID {article.id}...")


@app.delete("/articles/{article_id}")
def create_article(article_id: int, db: Session = Depends(get_db)):
    return crud.delete_article(db=db, article_id=article_id)
