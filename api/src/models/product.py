import uuid

from sqlalchemy import String, DECIMAL, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects import postgresql

from src.database import Base
from src.models.core_model import CoreModel


class Product(Base, CoreModel):
    __tablename__ = "products"

    name: Mapped[str] = mapped_column(String(128), nullable=False)
    code: Mapped[str] = mapped_column(String(128), nullable=False)
    group: Mapped[str] = mapped_column(String(128), nullable=False)
    description: Mapped[str] = mapped_column(String(128), nullable=False)
    photo_id: Mapped[uuid] = mapped_column(postgresql.UUID(as_uuid=True), ForeignKey("products.uuid"))
    quantity_in_stock: Mapped[int] = mapped_column(Integer, default=None, nullable=False)
    price: Mapped[float] = mapped_column(DECIMAL, nullable=False)
