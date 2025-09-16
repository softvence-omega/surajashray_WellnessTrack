from typing import TypedDict, Optional
from .meal_evaluation import Evaluation

class MealState(TypedDict):
    image_base64: str
    nutrition: Optional[Evaluation]