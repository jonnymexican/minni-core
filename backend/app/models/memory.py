from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.db.database import Base


class Memory(Base):

    __tablename__ = "memories"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        String,
        index=True
    )

    content = Column(
        String
    )
