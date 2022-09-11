from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from . import service
from core.auth import current_active_user
from users.models import User
from core.db import get_async_session
from .schemas import GameCreate, GameList

router = APIRouter()


@router.post("/api/games", response_model=GameCreate)
async def create_game(item: GameCreate, session: AsyncSession = Depends(get_async_session),
                      user: User = Depends(current_active_user)):
    return await service.create_game(session, item)


@router.get("/api/games", response_model=List[GameList])
async def get_games(session: AsyncSession = Depends(get_async_session), user: User = Depends(current_active_user)):
    return await service.get_games(session)


@router.delete("/api/games/{pk}")
async def delete_game(pk: int, session: AsyncSession = Depends(get_async_session),
                      user: User = Depends(current_active_user)):
    result = await service.delete_game(pk, session)
    if result is not None:
        return {'deleted': result}
    else:
        raise HTTPException(status_code=404, detail="Game not found")
