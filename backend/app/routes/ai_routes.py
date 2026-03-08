from fastapi import APIRouter, Depends
from app.schemas.ai_schema import AIRequest, AIResponse
from app.services.ai_service import ask_ai
from app.core.auth import get_current_user
from app.services.chat_service import save_chat
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter()

@router.post("/ask-ai", response_model=AIResponse)
def ask_ai_route(
    request: AIRequest,
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    answer = ask_ai(request.question)

    save_chat(db, current_user, request.question, answer)

    return {"answer": answer}