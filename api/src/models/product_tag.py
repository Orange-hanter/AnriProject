import uuid

from sqlalchemy import ForeignKey
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import relationship, mapped_column, Mapped

from src.database import Base
from src.models.core_model import CoreModel


class ProductTag(Base, CoreModel):
    __tablename__ = "product_tags"

    product_uuid: Mapped[uuid] = mapped_column(postgresql.UUID(as_uuid=True), ForeignKey("products.uuid"))
    product: Mapped["Product"] = relationship(back_populates="product_tags")
    tag_uuid: Mapped[uuid] = mapped_column(postgresql.UUID(as_uuid=True), ForeignKey("tags.uuid"))
    tag: Mapped["Tag"] = relationship(back_populates="product_tags")
