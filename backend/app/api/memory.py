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
        content=payload.content,
        source_type=payload.source_type,
        source_name=payload.source_name,
        source_uri=payload.source_uri,
        category=payload.category,
    )

    db.add(memory)

    db.commit()

    db.refresh(memory)

    return {
        "status": "stored",
        "id": memory.id,
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
                    "content": memory.content,
                    "source_type": memory.source_type,
                    "category": memory.category,
                }
            )

    return results


@router.get("/memory/{memory_id}")
def get_memory(
    memory_id: int,
    db: Session = Depends(get_db)
):

    memory = (
        db.query(Memory)
        .filter(
            Memory.id == memory_id
        )
        .first()
    )

    if memory is None:

        return {
            "error": "memory not found"
        }

    return {
        "id": memory.id,
        "user_id": memory.user_id,
        "content": memory.content,
        "source_type": memory.source_type,
        "source_name": memory.source_name,
        "source_uri": memory.source_uri,
        "category": memory.category,
        "created_at": str(memory.created_at),
    }


@router.get("/memories/{user_id}")
def list_memories(
    user_id: str,
    db: Session = Depends(get_db)
):

    memories = (
        db.query(Memory)
        .filter(
            Memory.user_id == user_id
        )
        .all()
    )

    return [
        {
            "id": memory.id,
            "content": memory.content,
            "source_type": memory.source_type,
            "source_name": memory.source_name,
            "category": memory.category,
            "created_at": str(
                memory.created_at
            ),
        }
        for memory in memories
    ]
