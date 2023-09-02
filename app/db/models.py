from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from .database import Base


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    text = Column(String)
    image = Column(String)
    is_publish = Column(Boolean, default=False)
    author_id = Column(ForeignKey("authors.id"), nullable=False)


class Author(Base):
    __tablename__ = "authors"
    
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)

