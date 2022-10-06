# Здесь бизнес логика, в виде классов или методов.
# Сюда импортируются DAO классы из пакета dao и модели из dao.model
# Некоторые методы могут оказаться просто прослойкой между dao и views,
# но чаще всего будет какая-то логика обработки данных сейчас или в будущем.
from typing import Optional
from flask_restx import abort
from project.dao.user import UsersDAO
from project.exceptions import ItemNotFound
from project.setup.db.user import User
from project.tools.security import generate_password_hash, compose_passwords


class UsersService:
    def __init__(self, dao: UsersDAO) -> None:
        self.dao = dao

    def create(self, data: dict) -> User:
        # Тут вся логика криэйта
        # Шифруем пароль
        data['password'] = generate_password_hash(data.get('password'))
        return self.dao.create(data)

    def update(self, email: str, data: dict) -> User:
        # Тут вся логика апдейта
        user = self.get_by_email(email)
        password = data.get("password", None)
        if password:
            del data["password"]
        [setattr(user, key, value) for key, value in data.items()]
        return self.dao.update(user)

    def password_update(self, email: str, data: dict) -> User:
        # Тут вся логика апдейта
        user = self.get_by_email(email)
        if user is None:
            raise ItemNotFound(f'User with email={email} not exists.')
        old_password = data.get('old_password')
        new_password = data.get('new_password')
        if not compose_passwords(user.password, old_password):
            raise abort(400)
        user.password = generate_password_hash(new_password)
        return self.dao.update(user)

    def get_by_email(self, email: str) -> Optional[User]:
        return self.dao.get_by_email(email)
