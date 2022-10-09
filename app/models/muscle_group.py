import typing as t

from pydantic import BaseModel


class MuscleGroup(BaseModel):
    name: str
