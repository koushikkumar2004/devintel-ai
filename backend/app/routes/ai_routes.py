from fastapi import APIRouter, Depends
from app.schemas.ai_schema import AIRequest, AIResponse
from app.services.ai_service import ask_ai
from app.core.auth import get_current_user

router = APIRouter()

@router.post("/ask-ai", response_model=AIResponse)
def ask_ai_route(request: AIRequest, current_user: str = Depends(get_current_user)):

    answer = ask_ai(request.question)

    return {"answer": answer}