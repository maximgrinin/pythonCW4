# Здесь бизнес логика, в виде классов или методов.
# Сюда импортируются DAO классы из пакета dao и модели из dao.model
# Некоторые методы могут оказаться просто прослойкой между dao и views,
# но чаще всего будет какая-то логика обработки данных сейчас или в будущем.
from typing import Optional
from project.dao.genre import GenresDAO
from project.exceptions import ItemNotFound
from project.setup.db.genre import Genre


class GenresService:
    def __init__(self, dao: GenresDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> Genre:
        if genre := self.dao.get_by_id(pk):
            return genre
        raise ItemNotFound(f'Genre with pk={pk} not exists.')

    def get_all(self, page: Optional[int] = None) -> list[Genre]:
        return self.dao.get_all(page=page)
