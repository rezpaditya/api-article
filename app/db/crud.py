from sqlalchemy.orm import Session
from . import models, schemas


def get_by_id(db: Session, dao, id: int):
    return db.query(dao).filter(dao.id == id).first()


def get(db: Session, dao, skip: int = 0, limit: int = 100):
    return db.query(dao).offset(skip).limit(limit).all()


def create(db: Session, dao):
    db.add(dao)
    db.commit()
    db.refresh(dao)
    return dao


def update(db: Session, dao, schema):
    db_data = db.query(dao).filter(dao.id == schema.id)
    db_data.update(schema.dict(exclude_unset=True))
    db.commit()
    return db_data.first()


def delete(db: Session, dao, id: int):
    effected_rows = db.query(dao).filter(dao.id == id).delete()
    db.commit()
    return bool(effected_rows > 0)