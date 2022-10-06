# Здесь бизнес логика, в виде классов или методов.
# Сюда импортируются DAO классы из пакета dao и модели из dao.model
# Некоторые методы могут оказаться просто прослойкой между dao и views,
# но чаще всего будет какая-то логика обработки данных сейчас или в будущем.
from typing import Optional
from project.dao.movie import MoviesDAO
from project.exceptions import ItemNotFound
from project.setup.db.movie import Movie


class MoviesService:
    def __init__(self, dao: MoviesDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> Movie:
        if movie := self.dao.get_by_id(pk):
            return movie
        raise ItemNotFound(f'Movie with pk={pk} not exists.')

    def get_all(self, page: Optional[int] = None, status: Optional[str] = None) -> list[Movie]:
        return self.dao.get_all(page=page, status=status)

    # def create(self, data):
    #     return self.dao.create(data)
    #
    # def update(self, mid, data):
    #     # Тут вся логика апдейта
    #     movie = self.get_item(mid)
    #     [setattr(movie, key, value) for key, value in data.items()]
    #     self.dao.update(movie)
    #     return self.dao
    #
    # def delete(self, mid):
    #     self.dao.delete(mid)
