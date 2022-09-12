from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import query

from games.models import Game
from users.models import User
from users_games.models import UserGame


async def connect_to_game(game_id: int, session: AsyncSession, user: User):
    game = await session.get(Game, game_id)
    if game is not None:
        user_game = UserGame(player=user.id, game=game.id)
        session.add(user_game)
        await session.commit()
        return user_game
    else:
        return None


async def disconnect_from_game(game_id: int, session: AsyncSession, user: User):
    select = query.Query(UserGame, session).filter(UserGame.player == user.id).filter(UserGame.game == game_id)
    result = await session.execute(select)
    for res in result:
        for user_game in res:
            try:
                await session.delete(user_game)
                await session.commit()
                return True
            except Exception:
                await session.rollback()
                return False
    return None


async def get_users_games(session: AsyncSession):
    result = await session.execute('SELECT g.id as game_id, g.name as game_name,'
                                   ' u.id as user_id, u.name as user_name, u.email, u.age from users_games as ug'
                                   '    inner join games as g'
                                   '        on ug.game = g.id'
                                   '    inner join "user" as u'
                                   '    on ug.player = u.id'
                                   ' ORDER BY'
                                   '    g.name, u.name')

    game_list = []
    last_game_id = None
    last_game_name = None
    players_list = []

    for g in result:
        if last_game_id is not None and g.game_id != last_game_id:
            game_list.append({
                'id': last_game_id,
                'name': last_game_name,
                'players': players_list
            })
            players_list = []

        players_list.append({
            'id': g.user_id,
            'name': g.user_name,
            'email': g.email,
            'age': g.age
        })
        last_game_id = g.game_id
        last_game_name = g.game_name

    if len(players_list) != 0:
        game_list.append({
            'id': last_game_id,
            'name': last_game_name,
            'players': players_list
        })

    return game_list


async def get_me(session: AsyncSession, user: User):
    result = await session.execute("SELECT g.id, g.name from users_games as ug"
                                   "    inner join games as g"
                                   "        on ug.game = g.id"
                                   f" WHERE ug.player = '{user.id}'"
                                   " ORDER BY"
                                   "    g.name")

    game_list = []
    for g in result:
        game_list.append({
            'id': g.id,
            'name': g.name
        })

    return {
        'id': user.id,
        'name': user.name,
        'email': user.email,
        'age': user.age,
        'games': game_list
    }
