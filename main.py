from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
import models
from api import movie
from database import SessionLocal, engine


app = FastAPI(title="MovieRestFullAPI")

app.include_router(movie.router, tags=["movie"])


@app.on_event("startup")
def startup_event():
    models.Base.metadata.create_all(bind=engine)
    db: Session = SessionLocal()
    db.close()
