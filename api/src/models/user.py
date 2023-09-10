from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from sqlalchemy import String, Column

from src.database import Base


class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "users"

    username = Column(String(64), nullable=False)
