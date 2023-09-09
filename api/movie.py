from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
import deps
from schemas import movies_schemas
from repository.movie_repository import MovieRepository
from schemas import DateQueryParam

router = APIRouter()


@router.get("/movie/", response_model=List[movies_schemas.MovieList])
async def read_movies(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(
        deps.get_db,
    ),
):
    movies = MovieRepository.get_movies(db, skip=skip, limit=limit)
    return movies


@router.post("/movie/", response_model=movies_schemas.MovieList)
async def create_movie(
    item: movies_schemas.MovieRequest,
    db: Session = Depends(deps.get_db),
):
    return MovieRepository.create_movie(db=db, movie=item)


@router.get("/movie/{id}/", response_model=movies_schemas.MovieList)
async def read_detail_movie(id: int, db: Session = Depends(deps.get_db)):
    db_movie = MovieRepository.get_movie(db, id=id)
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return db_movie


@router.get("/search-movie/{name}/", response_model=movies_schemas.MovieList)
async def read_detail_movie(name: str, db: Session = Depends(deps.get_db)):
    db_movie = MovieRepository.get_movie_by_name(db, name=name)
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return db_movie


@router.patch("/movie/{id}/", response_model=movies_schemas.MovieList)
async def update_patch_movie(
    id: int, item: movies_schemas.MovieRequest, db: Session = Depends(deps.get_db)
):
    db_movie = MovieRepository.update_movie(db, id=id, movie=item)
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return db_movie


@router.put("/movie/{id}/", response_model=movies_schemas.MovieList)
async def update_movie(
    id: int, item: movies_schemas.MovieRequest, db: Session = Depends(deps.get_db)
):
    db_movie = MovieRepository.update_movie(db, id=id, movie=item)
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return db_movie


@router.delete("/movie/{id}/")
async def delete_movie(id: int, db: Session = Depends(deps.get_db)):
    db_movie = MovieRepository.delete_movie(db, id=id)
    if db_movie is None:
        raise HTTPException(status_code=200, detail="succes delete")
    return db_movie
