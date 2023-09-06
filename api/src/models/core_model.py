import uuid

from sqlalchemy import Column, func
from sqlalchemy.types import DateTime
from sqlalchemy.dialects import postgresql


class CoreModel:
    __abstract__ = True

    uuid = Column(postgresql.UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    created = Column(DateTime, nullable=False, default=func.now())
    updated = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())
