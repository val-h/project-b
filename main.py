import json
import typing as t

import fastapi

# Models
from app.models.exercise import Exercise

app = fastapi.FastAPI()


@app.get("/")
async def home() -> dict:
    return {"data": "Hello, World!"}


@app.get("/test/{id}")
async def random_data(
        id: int = fastapi.Path(description="Just a description for schema", ge=0, lt=1000),
        q: str | None = fastapi.Query(defaut=None, title="Title", alias="test-query", max_length=20, deprecated=True)) -> dict:
    data: t.Dict[str, t.Any] = {"id": id}
    if q:
        data.update({"_q": q})
    return data


@app.put("/exercises/{id}")
async def get_exercise(id: int, exercise: Exercise) -> dict:
    return exercise.dict()
