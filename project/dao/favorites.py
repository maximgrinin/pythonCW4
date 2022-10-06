# Это файл для классов доступа к данным (Data Access Object).
# Здесь должен быть класс с методами доступа к данным.
# Здесь в методах можно построить сложные запросы к БД.
from typing import List
from project.dao.base import BaseDAO
from project.setup.db.favorites import Favorites


class FavoritesDAO(BaseDAO[Favorites]):
    __model__ = Favorites

    def get_by_user(self, uid: int) -> List[__model__]:
        favorites: List[Favorites] | [] = self._db_session.query(self.__model__).filter(Favorites.user_id == uid).all()
        return favorites

    def get_by_user_and_movie(self, mid: int, uid: int) -> List[__model__]:
        favorites: List[Favorites] | [] = self._db_session.query(self.__model__).\
            filter(Favorites.user_id == uid, Favorites.movie_id == mid).all()
        return favorites

    def create(self, data: dict) -> __model__:
        new_favorites = self.__model__(**data)
        self._db_session.add(new_favorites)
        self._db_session.commit()
        return new_favorites

    def delete(self, mid: int, uid: int):
        favorites = self.get_by_user_and_movie(mid, uid)
        for item in favorites:
            self._db_session.delete(item)
        self._db_session.commit()
