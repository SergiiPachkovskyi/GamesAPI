from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from sqlalchemy import Column, String, Integer

from core.base import Base


class User(SQLAlchemyBaseUserTableUUID, Base):
    name = Column(String)
    age = Column(Integer)
