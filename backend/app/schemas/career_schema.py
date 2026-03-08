from pydantic import BaseModel
from typing import List


class CareerRequest(BaseModel):
    skills: List[str]
    interests: List[str]
    education: str


class CareerResponse(BaseModel):
    career_advice: str
    