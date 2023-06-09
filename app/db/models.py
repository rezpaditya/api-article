from sqlalchemy import Column, String, Integer, Boolean
from .database import Base


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    text = Column(String)
    image = Column(String)
    is_publish = Column(Boolean, default=False)
