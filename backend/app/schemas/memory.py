from pydantic import BaseModel


class MemoryCreate(BaseModel):

    user_id: str

    content: str

    source_type: str = "text"

    source_name: str | None = None

    source_uri: str | None = None

    category: str = "general"


class MemorySearch(BaseModel):

    user_id: str

    query: str
