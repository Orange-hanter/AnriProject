import uuid
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from ..database import Base
from . import core_model


class Employee(Base, core_model.CoreModel):
    __tablename__ = 'employees'

    contragent_uuid: Mapped[uuid] = mapped_column(postgresql.UUID(as_uuid=True), ForeignKey("contragents.uuid"))
    contragent: Mapped['Contragent'] = mapped_column(relationship(back_populates='employees'))
    user_uuid: Mapped[uuid] = mapped_column(postgresql.UUID(as_uuid=True), ForeignKey("users.uuid"))
    user: Mapped['User'] = mapped_column(relationship(back_populates='employees'))
