from pydantic import BaseModel


class MemoryCreate(BaseModel):
    user_id: str
    content: str


class MemorySearch(BaseModel):
    user_id: str
    query: str
