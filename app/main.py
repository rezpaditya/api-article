from fastapi import FastAPI
from app.db import models
from app.db.database import engine
from fastapi.middleware.cors import CORSMiddleware
from app.router import author, article

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:4200",
    "https://blog.respa.nl",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# include all router
app.include_router(author.router)
app.include_router(article.router)
