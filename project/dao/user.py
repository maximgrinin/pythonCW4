# Это файл для классов доступа к данным (Data Access Object).
# Здесь должен быть класс с методами доступа к данным.
# Здесь в методах можно построить сложные запросы к БД.
from typing import Optional
from project.dao.base import BaseDAO
from project.exceptions import ItemNotFound
from project.setup.db.user import User


class UsersDAO(BaseDAO[User]):
    __model__ = User

    def create(self, data: dict) -> __model__:
        new_user = self.__model__(**data)
        self._db_session.add(new_user)
        self._db_session.commit()
        return new_user

    def update(self, user: __model__) -> __model__:
        self._db_session.add(user)
        self._db_session.commit()
        return user

    def get_by_email(self, email: str) -> Optional[__model__]:
        if user := self._db_session.query(self.__model__).filter(User.email == email).first():
            return user
        raise ItemNotFound(f'User with email={email} not exists.')
