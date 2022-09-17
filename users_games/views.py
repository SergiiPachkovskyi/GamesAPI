from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from . import service
from core.auth import current_active_user
from users.models import User
from core.db import get_async_session
from .schemas import UserGameCreate, GamesWithUsers, UserWithGames

router = APIRouter()


@router.post("/api/connect/{game_id}", response_model=UserGameCreate)
async def connect_to_game(game_id: int, session: AsyncSession = Depends(get_async_session),
                          user: User = Depends(current_active_user)):
    result = await service.connect_to_game(game_id, session, user)
    if result is not None:
        return result
    else:
        raise HTTPException(status_code=404, detail="Game not found")


@router.delete("/api/disconnect/{game_id}")
async def disconnect_from_game(game_id: int, session: AsyncSession = Depends(get_async_session),
                               user: User = Depends(current_active_user)):
    result = await service.disconnect_from_game(game_id, session, user)

    if result is not None:
        return {'disconnect': result}
    else:
        raise HTTPException(status_code=404, detail="Connected game not found")


@router.get("/api/get_games", response_model=list[GamesWithUsers])
async def get_users_games(session: AsyncSession = Depends(get_async_session),
                          user: User = Depends(current_active_user)):
    return await service.get_users_games(session)


@router.get("/api/get_me", response_model=UserWithGames)
async def get_me(session: AsyncSession = Depends(get_async_session), user: User = Depends(current_active_user)):
    return await service.get_me(session, user)
