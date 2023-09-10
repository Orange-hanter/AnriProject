from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Column

from src.database import Base
from src.models import core_model


class Employee(Base, core_model.CoreModel):
    __tablename__ = "employees"

    contragent_uuid = Column(postgresql.UUID(as_uuid=True), ForeignKey("contragents.uuid"))
    contragent = relationship("Contragent", back_populates="employees")
    user_uuid = Column(postgresql.UUID(as_uuid=True), ForeignKey("users.uuid"))
    user = relationship("User", back_populates="employees")
