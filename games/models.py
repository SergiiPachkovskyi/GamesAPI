from sqlalchemy import Column, String, Integer

from core.base import Base


class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String)
