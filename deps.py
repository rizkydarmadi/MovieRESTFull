from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError
from sqlalchemy.orm import Session
from starlette import status
import models, security
from database import SessionLocal
from settings import Settings


reusable_oauth2 = OAuth2PasswordBearer(tokenUrl="/login/access-token")


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
