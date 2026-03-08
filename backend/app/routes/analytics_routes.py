from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.analytics_service import get_user_stats
from app.core.auth import get_current_user

router = APIRouter()

@router.get("/user-stats")
def user_stats(
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    stats = get_user_stats(db, current_user)

    return stats