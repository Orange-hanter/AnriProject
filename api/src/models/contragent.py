from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Float

from src.database import Base
from src.models import core_model


class Contragent(Base, core_model.CoreModel):
    __tablename__ = "contragents"

    company_name: Mapped[str] = mapped_column(String, nullable=False)
    state_cadastr_code: Mapped[str] = mapped_column(String, nullable=False)
    legal_address: Mapped[str] = mapped_column(String, nullable=False)
    company_rating: Mapped[str] = mapped_column(Float, nullable=False, default=None)
    contact_name: Mapped[str] = mapped_column(String, nullable=False)
    contact_email: Mapped[str] = mapped_column(String, nullable=False)
    contact_phone: Mapped[str] = mapped_column(String, nullable=False)
