from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.models.memory import Memory

from app.core.profile_builder import (
    ProfileBuilder
)

router = APIRouter()


def get_db():

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.get("/profile/{user_id}")
def profile(
    user_id: str,
    db: Session = Depends(get_db)
):

    memories = (
        db.query(Memory)
        .filter(
            Memory.user_id ==
            user_id
        )
        .all()
    )

    return ProfileBuilder.build(
        memories
    )
