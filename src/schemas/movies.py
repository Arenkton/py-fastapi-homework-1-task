from datetime import date

from pydantic import BaseModel, ConfigDict


class MovieDetailResponseSchema(BaseModel):
    movies: list[MovieDetailResponseSchema]
    prev_page: str | None = None
    next_page: str | None = None
    total_pages: int
    total_items: int
    id: int
    name: str
    date: date | None = None
    score: float | None = None
    genre: str | None = None
    overview: str | None = None
    crew: str | None = None
    orig_title: str | None = None
    status: str | None = None
    orig_lang: str | None = None
    budget: float | None = None
    revenue: float | None = None
    country: str | None = None

    model_config = ConfigDict(from_attributes=True)
