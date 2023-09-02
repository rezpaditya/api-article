from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db import schemas, models, crud
from app.dependencies import get_db


router = APIRouter(
    prefix="/articles",
    tags=["articles"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=list[schemas.Article])
def read_articles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    articles = crud.get(db, dao=models.Article, skip=skip, limit=limit)
    if articles:
        return articles
    else:
        raise HTTPException(status_code=404, detail="failed to fetch articles...")
    

@router.get("/{article_id}", response_model=schemas.Article)
def read_articles(article_id, db: Session = Depends(get_db)):
    article = crud.get_by_id(db, dao=models.Article, id=article_id)
    if article:
        return article
    else:
        raise HTTPException(status_code=404, detail=f"Article ID {article_id} is not found...")


@router.post("/", response_model=schemas.Article)
def create_article(article: schemas.Article, db: Session = Depends(get_db)):
    dao = models.Article(title=article.title, text=article.text, image=article.image, author_id=article.author_id)
    db_article = crud.create(db=db, dao=dao)
    if db_article:
        return db_article
    else:
        raise HTTPException(status_code=401, detail="Failed to create article...")


@router.patch("/", response_model=schemas.Article)
def update_article(article: schemas.Article, db: Session = Depends(get_db)):
    db_article = crud.update(db=db, dao=models.Article, schema=article)
    if db_article:
        return db_article
    else:
        raise HTTPException(status_code=401, detail=f"Failed to update article with ID {article.id}...")


@router.delete("/{article_id}")
def delete_article(article_id: int, db: Session = Depends(get_db)):
    return crud.delete(db=db, dao=models.Article, id=article_id)