from pydantic import BaseModel


class GameBase(BaseModel):
    name: str

    class Config:
        orm_mode = True


class GameCreate(GameBase):
    pass


class GameRead(GameBase):
    id: int


