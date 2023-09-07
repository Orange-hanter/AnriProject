from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from sqlalchemy import Column, String

from ..database import Base, metadata


class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = 'users'

    username = Column(String)
    password = Column(String)
