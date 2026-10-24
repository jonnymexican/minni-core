from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.db.database import SessionLocal

from app.models.memory import Memory

from app.schemas.memory import (
    MemorySearch
)

from app.core.profile_builder import (
    ProfileBuilder
)

from app.core.context_builder import (
    ContextBuilder
)

router = APIRouter()


def get_db():

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.post("/context")
def context(
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

    memory_results = [
        {
            "id": memory.id,
            "content": memory.content
        }
        for memory in memories
    ]

    profile = (
        ProfileBuilder.build(memories)
    )

    context_text = (
        ContextBuilder.build(
            payload.query,
            profile,
            memory_results
        )
    )

    return {
        "profile": profile,
        "relevant_memories":
        memory_results,
        "context":
        context_text
    }
