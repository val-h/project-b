from enum import Enum
import typing as t

from pydantic import BaseModel

from .muscle_group import MuscleGroup

class ExerciseType(str, Enum):
    BODYWEIGHT = "bodyweight"
    WEIGHTED = "weighted"
    CARDIO = "cardio"


class Exercise(BaseModel):
    name: str
    muscle_groups: t.List[t.Optional[MuscleGroup]]
    exercise_type: t.Optional[ExerciseType]
    dificulty: t.Optional[str]
