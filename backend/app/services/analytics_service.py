from sqlalchemy.orm import Session
from app.models.chat import Chat

def get_user_stats(db: Session, email: str):

    total_questions = db.query(Chat).filter(Chat.user_email == email).count()

    career_requests = db.query(Chat).filter(
        Chat.user_email == email,
        Chat.question.ilike("%career%")
    ).count()

    return {
        "total_questions": total_questions,
        "career_requests": career_requests,
        "chat_history_count": total_questions
    }