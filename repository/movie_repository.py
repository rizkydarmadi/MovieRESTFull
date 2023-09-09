from sqlalchemy.orm import Session
import models
from schemas import movies_schemas
from datetime import datetime
from sqlalchemy import delete


class MovieRepository:
    @staticmethod
    def create_movie(db: Session, movie: movies_schemas.MovieRequest):
        db_movie = models.Movie(
            title=movie.title,
            description=movie.description,
            rating=movie.rating,
            image=movie.image,
            created_at=datetime.now(),
            updated_at=None,
        )
        db.add(db_movie)
        db.commit()
        db.refresh(db_movie)
        return db_movie

    @staticmethod
    def get_movies(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.Movie).offset(skip).limit(limit).all()

    @staticmethod
    def get_movie(db: Session, id: int):
        return db.query(models.Movie).filter(models.Movie.id == id).first()

    @staticmethod
    def get_movie_by_name(db: Session, name: str):
        return (
            db.query(models.Movie).filter(models.Movie.title.ilike(f"%{name}%")).first()
        )

    @staticmethod
    def update_movie(db: Session, movie: movies_schemas.MovieRequest, id: int):
        movie_object: models.Movie = (
            db.query(models.Movie).filter(models.Movie.id == id).first()
        )

        movie_object.title = movie.title
        movie_object.description = movie.description
        movie_object.rating = movie.rating
        movie_object.image = movie.image
        movie_object.updated_at = datetime.now()

        db.add(movie_object)
        db.commit()
        db.refresh(movie_object)
        return movie_object

    @staticmethod
    def delete_movie(db: Session, id: int):
        db.query(models.Movie).filter(models.Movie.id == id).delete()
        db.commit()
