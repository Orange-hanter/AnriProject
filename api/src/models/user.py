from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from src.database import Base


class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(String(64), nullable=False)
