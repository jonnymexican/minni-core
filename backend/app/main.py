from fastapi import FastAPI

from app.db.database import (
    Base,
    engine
)

from app.api.memory import (
    router as memory_router
)

from app.api.profile import (
    router as profile_router
)

from app.api.context import (
    router as context_router
)

Base.metadata.create_all(
    bind=engine
)

app = FastAPI(
    title="Minni"
)

app.include_router(
    memory_router
)

app.include_router(
    profile_router
)

app.include_router(
    context_router
)


@app.get("/")
def root():

    return {
        "name": "Minni",
        "status": "ok"
    }
