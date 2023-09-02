from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db import schemas, models, crud
from app.dependencies import get_db


router = APIRouter(
    prefix="/authors",
    tags=["authors"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=list[schemas.Author])
def get_authors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    authors = crud.get(db, dao=models.Author, skip=skip, limit=limit)
    if authors:
        return authors
    else:
        raise HTTPException(status_code=404, detail="failed to fetch authors...")
    

@router.get("/{author_id}", response_model=schemas.Author)
def read_author(author_id, db: Session = Depends(get_db)):
    author = crud.get_by_id(db, dao=models.Author, id=author_id)
    if author:
        return author
    else:
        raise HTTPException(status_code=404, detail=f"Author ID {author_id} is not found...")
  

@router.post("/", response_model=schemas.Author)
def create_author(author: schemas.Author, db: Session = Depends(get_db)):
    dao = models.Author(first_name=author.first_name, last_name=author.last_name)
    db_author = crud.create(db=db, dao=dao)
    if db_author:
        return db_author
    else:
        raise HTTPException(status_code=401, detail="Failed to create author...")


@router.patch("/", response_model=schemas.Author)
def update_author(author: schemas.Author, db: Session = Depends(get_db)):
    db_author = crud.update(db=db, dao=models.Author, schema=author)
    if db_author:
        return db_author
    else:
        raise HTTPException(status_code=401, detail=f"Failed to update author with ID {author.id}...")


@router.delete("/{author_id}")
def delete_author(author_id: int, db: Session = Depends(get_db)):
    return crud.delete(db=db, dao=models.Author, id=author_id)