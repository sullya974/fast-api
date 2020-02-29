from typing import List
from pydantic import BaseModel


class RedWineRequest(BaseModel):
    fixed_acidity: float
    volatile_acidity: float
    citric_acid: float
    residual_sugar: float
    chlorides: float
    free_sulfur_dioxide: float
    total_sulfur_dioxide: float
    density: float
    pH: float
    sulphates: float
    alcohol: float


# One class for the response expected
# Class for the response of the sagemaker endpoint.
class RedWineResponse(BaseModel):
    quality:List[float]

# class RedWineRequest(BaseModel):
#     fixed_acidity: float
#     #todo : define the other inputs of your Request and response

# class RedWineResponse(BaseModel):
