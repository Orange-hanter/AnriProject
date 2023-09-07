from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped

from src.database import Base
from src.models.core_model import CoreModel


class Tag(Base, CoreModel):
    __tablename__ = "tags"

    name: Mapped[str] = mapped_column(String(128), nullable=False)
