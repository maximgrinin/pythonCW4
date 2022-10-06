# Здесь бизнес логика, в виде классов или методов.
# Сюда импортируются DAO классы из пакета dao и модели из dao.model
# Некоторые методы могут оказаться просто прослойкой между dao и views,
# но чаще всего будет какая-то логика обработки данных сейчас или в будущем.
from project.dao.favorites import FavoritesDAO
from project.setup.db.favorites import Favorites


class FavoritesService:
    def __init__(self, dao: FavoritesDAO) -> None:
        self.dao = dao

    def get_all_by_user(self, uid: int) -> list[Favorites]:
        return self.dao.get_by_user(uid)

    def create(self, mid: int, uid: int) -> Favorites:
        data = {
            "user_id": uid,
            "movie_id": mid
        }
        return self.dao.create(data)

    def delete(self, mid: int, uid: int):
        self.dao.delete(mid, uid)
