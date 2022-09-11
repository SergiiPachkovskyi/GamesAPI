from fastapi_users_db_sqlalchemy.generics import GUID

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from core.base import Base
from users.models import User
from games.models import Game


class UserGame(Base):
    __tablename__ = 'users_games'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    player = Column(GUID, ForeignKey('user.id'))
    player_id = relationship(User)
    game = Column(Integer, ForeignKey('games.id'))
    game_id = relationship(Game)
