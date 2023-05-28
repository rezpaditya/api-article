from sqlalchemy.orm import Session

from . import models, schemas


def get_article(db: Session, article_id: int):
    return db.query(models.Article).filter(models.Article.id == article_id).first()


def get_articles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Article).offset(skip).limit(limit).all()


def create_article(db: Session, article: schemas.ArticleCreate):
    db_article = models.Article(title=article.title, text=article.text, image=article.image)
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article