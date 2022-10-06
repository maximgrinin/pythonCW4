# Это файл для классов доступа к данным (Data Access Object).
# Здесь должен быть класс с методами доступа к данным.
# Здесь в методах можно построить сложные запросы к БД.
from typing import List, Optional
from flask_sqlalchemy import BaseQuery
from werkzeug.exceptions import NotFound
from project.dao.base import BaseDAO
from project.setup.db.movie import Movie


class MoviesDAO(BaseDAO[Movie]):
    __model__ = Movie

    def get_all(self, page: Optional[int] = None, status: Optional[str] = None) -> List[__model__]:
        stmt: BaseQuery = self._db_session.query(self.__model__)
        if status == 'new':
            stmt = stmt.order_by(self.__model__.created.desc())
        if page:
            try:
                return stmt.paginate(page, self._items_per_page).items
            except NotFound:
                return []
        return stmt.all()
