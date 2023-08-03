from pydantic import BaseModel, field_serializer
from datetime import datetime


class MovieList(BaseModel):
    id: int
    title: str
    description: str
    rating: float
    image: str
    created_at: datetime
    updated_at: datetime | None

    @field_serializer("created_at")
    def serialize_dt(self, created_at: datetime, _info):
        return created_at.isoformat()

    @field_serializer("updated_at")
    def serialize_dt(self, updated_at: datetime, _info):
        return updated_at.isoformat() if updated_at != None else None


class MovieRequest(BaseModel):
    title: str
    description: str
    rating: float
    image: str

    class Config:
        from_attributes = True
