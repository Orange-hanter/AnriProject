from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Float, Column

from src.database import Base
from src.models import core_model


class Contragent(Base, core_model.CoreModel):
    __tablename__ = "contragents"

    company_name = Column(String, nullable=False)
    state_cadastr_code = Column(String, nullable=False)
    legal_address = Column(String, nullable=False)
    company_rating = Column(Float, nullable=False, default=None)
    contact_name = Column(String, nullable=False)
    contact_email = Column(String, nullable=False)
    contact_phone = Column(String, nullable=False)
