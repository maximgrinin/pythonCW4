from project.config import config
from project.setup.db.genre import Genre
from project.setup.db.director import Director
from project.setup.db.movie import Movie
from project.setup.db.user import User
from project.setup.db.favorites import Favorites
from project.server import create_app, db

if __name__ == '__main__':
    app = create_app(config)
    app.run(host="localhost", port=5000)

# app = create_app(config)


@app.shell_context_processor
def shell():
    return {
        "db": db,
        "Genre": Genre,
        "Director": Director,
        "Movie": Movie,
        "User": User,
        "Favorites": Favorites,
    }
