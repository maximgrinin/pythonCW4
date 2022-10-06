from load_fixtures import load_data
from project.config import config
from project.setup.db.genre import Genre
from project.setup.db.director import Director
from project.setup.db.movie import Movie
from project.setup.db.user import User
from project.setup.db.favorites import Favorites
from project.server import create_app, db
from typing import Any, Dict, List
from project.utils import read_json


if __name__ == '__main__':
    app = create_app(config)
    if app.config["SQLALCHEMY_DATABASE_URI"] ==  "sqlite:///:memory:":
        with app.app_context():
            db.create_all()
            fixtures: Dict[str, List[Dict[str, Any]]] = read_json("fixtures.json")
            load_data(fixtures['genres'], Genre)
            load_data(fixtures['directors'], Director)
            load_data(fixtures['movies'], Movie)
            db.session.commit()
    app.run(host="localhost", port=5000)


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
