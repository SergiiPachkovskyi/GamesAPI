import uuid

from fastapi_users import schemas
from pydantic import BaseModel, Field


class UserCreate(schemas.BaseUserCreate, BaseModel):
    name: str
    age: int = Field(gt=0, le=100)


class UserRead(schemas.BaseUser[uuid.UUID]):
    name: str
    age: int


class UserUpdate(schemas.BaseUserUpdate):
    name: str
    age: int


class UserShortInfo(BaseModel):
    id: uuid.UUID
    name: str
