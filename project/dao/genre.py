# Это файл для классов доступа к данным (Data Access Object).
# Здесь должен быть класс с методами доступа к данным
# Здесь в методах можно построить сложные запросы к БД
from project.dao.base import BaseDAO
from project.setup.db.genre import Genre


class GenresDAO(BaseDAO[Genre]):
    __model__ = Genre
