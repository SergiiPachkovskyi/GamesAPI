from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from games.models import Game
from games.schemas import GameCreate


async def create_game(session: AsyncSession, item: GameCreate):
    game = Game(name=item.name)
    session.add(game)
    await session.commit()
    return game


async def get_games(session: AsyncSession):
    result = await session.execute(select(Game))
    return result.scalars().all()


async def delete_game(pk: int, session: AsyncSession):
    game = await session.get(Game, pk)
    if game is not None:
        try:
            await session.delete(game)
            await session.commit()
            return True
        except Exception:
            await session.rollback()
            return False
    else:
        raise None
