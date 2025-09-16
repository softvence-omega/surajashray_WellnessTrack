from pydantic import BaseModel, Field, model_validator
from fastapi import HTTPException

class Evaluation(BaseModel):
    calories: int = Field(description="measure the calories")
    protein_g: int = Field(description="measure the protein in grams")
    carbs_g: int = Field(description="measure the carbs in grams")
    fats_g: int = Field(description="measure the fats in grams")
    is_meal: bool = Field(description="True if this is a meal image, False otherwise")


'''
    @model_validator(mode="before")
    def check_is_meal(cls, values):
        if not values.get("is_meal"):
            raise HTTPException(status_code=500, detail="The provided image is not recognized any meal.") 
        return values
'''