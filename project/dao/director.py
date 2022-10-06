# Это файл для классов доступа к данным (Data Access Object).
# Здесь должен быть класс с методами доступа к данным.
# Здесь в методах можно построить сложные запросы к БД.
from project.dao.base import BaseDAO
from project.setup.db.director import Director


class DirectorsDAO(BaseDAO[Director]):
    __model__ = Director

    # def create(self, data):
    #     new_director = Director(**data)
    #     self._db_session.add(new_director)
    #     self._db_session.commit()
    #     return new_director
    #
    # def update(self, director):
    #     self._db_session.add(director)
    #     self._db_session.commit()
    #     return director
    #
    # def delete(self, did):
    #     director = self.get_by_id(did)
    #     self._db_session.delete(director)
    #     self._db_session.commit()
