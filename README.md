# Project name
GamesAPI

# General info
API for games management

![](proj_news/app_news/static/images/API.png)

# Routes to implement
| METHOD   | ROUTE                           | FUNCTIONALITY                     |
|----------|---------------------------------|-----------------------------------|
| *POST*   | ```/auth/register```            | register new user                 |
| *POST*   | ```/auth/jwt/login```           | get jwt-tokens                    |
| *GET*    | ```/api/games```                | details of all games              |
| *POST*   | ```/api/games```                | create a game                     |
| *DELETE* | ```/api/games/{pk}```           | delete game                       |
| *POST*   | ```/api/connect/{game_id}```    | connect to game                   |
| *DELETE* | ```/api/disconnect/{game_id}``` | disconnect from game              |
| *GET*    | ```/api/get_games```            | get games and users               |
| *GET*    | ```/api/get_me```               | get indo about user and his games |


# Technologies
* Python 3
* FastAPI
* SQLAlchemy
* PostgreSQL
* JWT

# Setup

Run project
```
git clone https://github.com/SergiiPachkovskyi/GamesAPI

docker-compose build
docker-compose up
```

# Status
Project is: in progress
