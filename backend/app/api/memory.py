from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.models.memory import Memory
from app.schemas.memory import (
    MemoryCreate,
    MemorySearch
)

router = APIRouter()


def get_db():

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.post("/remember")
def remember(
    payload: MemoryCreate,
    db: Session = Depends(get_db)
):

    memory = Memory(
        user_id=payload.user_id,
        content=payload.content
    )

    db.add(memory)

    db.commit()

    db.refresh(memory)

    return {
        "status": "stored",
        "id": memory.id
    }


@router.post("/recall")
def recall(
    payload: MemorySearch,
    db: Session = Depends(get_db)
):

    memories = (
        db.query(Memory)
        .filter(
            Memory.user_id ==
            payload.user_id
        )
        .all()
    )

    results = []

    for memory in memories:

        if payload.query.lower() in memory.content.lower():

            results.append(
                {
                    "id": memory.id,
                    "content": memory.content
                }
            )

    return results
