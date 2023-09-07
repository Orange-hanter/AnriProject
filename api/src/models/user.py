from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from ..database import Base
from . import core_model


class User(SQLAlchemyBaseUserTableUUID, Base, core_model.CoreModel):
    __tablename__ = 'users'

    username: Mapped[str] = mapped_column(String(64), nullable=False)
