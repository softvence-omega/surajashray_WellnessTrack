from fastapi import HTTPException
import base64
from langgraph.graph import StateGraph, START, END
from ..config import base_model
from ..schemas.meal_evaluation import Evaluation
from ..schemas.mealstate import MealState

# Structured model
structured_model = base_model.with_structured_output(Evaluation)

def analyze_food(state: MealState) -> MealState:
    try:
        image_url = f"data:image/jpeg;base64,{state['image_base64']}"
        resp = structured_model.invoke(
            [
                {"role": "system", "content": "You are a nutrition expert."},
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Analyze this food image and return values in the schema"},
                        {"type": "image_url", "image_url": {"url": image_url}},
                    ],
                },
            ]
        )
        state["nutrition"] = resp
        return state
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
