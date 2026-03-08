from sqlalchemy.orm import Session
from app.models.chat import Chat

def save_chat(db: Session, email: str, question: str, answer: str):

    chat = Chat(
        user_email=email,
        question=question,
        answer=answer
    )

    db.add(chat)
    db.commit()
    db.refresh(chat)

    return chat


def get_chat_history(db: Session, email: str):

    return db.query(Chat).filter(Chat.user_email == email).all()