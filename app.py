import uvicorn
from fastapi import FastAPI

from core.db import create_db_and_tables
from users.views import router as users_router
from games.views import router as games_router
from users_games.views import router as users_games_router

app = FastAPI()


app.include_router(users_router)
app.include_router(games_router)
app.include_router(users_games_router)


@app.on_event("startup")
async def on_startup():
    # Not needed if you setup a migration system like Alembic
    await create_db_and_tables()


if __name__ == '__main__':
    uvicorn.run(
        'app:app',
        host='127.0.0.1',
        port=8000,
        log_level='info',
        loop='asyncio'
    )
