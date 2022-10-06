from project.dao.genre import GenresDAO
from project.dao.director import DirectorsDAO
from project.dao.movie import MoviesDAO
from project.dao.user import UsersDAO
from project.dao.favorites import FavoritesDAO

from project.services.genres_service import GenresService
from project.services.directors_service import DirectorsService
from project.services.movies_service import MoviesService
from project.services.users_service import UsersService
from project.services.auth_service import AuthService
from project.services.favorites_service import FavoritesService

from project.setup.db.setup_db import db

# DAO
genre_dao = GenresDAO(db.session)
director_dao = DirectorsDAO(db.session)
movie_dao = MoviesDAO(db.session)
user_dao = UsersDAO(db.session)
favorites_dao = FavoritesDAO(db.session)

# Services
genre_service = GenresService(dao=genre_dao)
director_service = DirectorsService(dao=director_dao)
movie_service = MoviesService(dao=movie_dao)
user_service = UsersService(dao=user_dao)
auth_service = AuthService(service=user_service)
favorites_service = FavoritesService(dao=favorites_dao)
