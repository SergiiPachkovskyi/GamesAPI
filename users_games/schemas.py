import uuid

from pydantic import BaseModel


class UserGameBase(BaseModel):
    id: int

    class Config:
        orm_mode = True


class UserGameCreate(UserGameBase):
    game: int
    player: uuid.UUID

