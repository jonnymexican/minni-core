from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
)

from app.db.database import Base


class Memory(Base):

    __tablename__ = "memories"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    user_id = Column(
        String,
        index=True,
        nullable=False,
    )

    content = Column(
        Text,
        nullable=False,
    )

    source_type = Column(
        String,
        default="text",
    )

    source_name = Column(
        String,
        nullable=True,
    )

    source_uri = Column(
        String,
        nullable=True,
    )

    category = Column(
        String,
        default="general",
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )
