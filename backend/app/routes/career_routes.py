from fastapi import APIRouter, Depends
from app.schemas.career_schema import CareerRequest, CareerResponse
from app.services.career_service import generate_career_advice
from app.core.auth import get_current_user

router = APIRouter()

@router.post("/career-advice", response_model=CareerResponse)
def career_advice(data: CareerRequest, current_user: str = Depends(get_current_user)):

    advice = generate_career_advice(
        data.skills,
        data.interests,
        data.education
    )

    return {"career_advice": advice}