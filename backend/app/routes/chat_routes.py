from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.chat_service import get_chat_history
from app.core.auth import get_current_user

router = APIRouter()

@router.get("/history")
def chat_history(
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    chats = get_chat_history(db, current_user)

    return chats