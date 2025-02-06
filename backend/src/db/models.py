import uuid
from dataclasses import dataclass
from typing import Iterable, Mapping


@dataclass
class Ingredient:
    uuid: uuid.UUID
    name: str
    serving: float
    serving_unit: str
    calories_per_serving: float
    protein_per_serving: float

    @classmethod
    def from_dict(cls, item):
        return cls(**item)


@dataclass
class Recipe:
    name: str
    ingredients_and_quantities: Mapping[Ingredient, float]


@dataclass
class DayPlan:
    day: str
    meals_and_recipes: Mapping[str, Iterable[Recipe]]
