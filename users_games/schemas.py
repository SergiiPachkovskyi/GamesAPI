import uuid

from pydantic import BaseModel

from games.schemas import GameRead
from users.schemas import UserRead, UserShortInfo


class UserGameBase(BaseModel):
    id: int

    class Config:
        orm_mode = True


class UserGameCreate(UserGameBase):
    game: int
    player: uuid.UUID


class GamesWithUsers(GameRead):
    players: list[UserRead]


class UserWithGames(UserShortInfo):
    games: list[GameRead]



