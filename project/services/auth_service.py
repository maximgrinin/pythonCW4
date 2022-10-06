# Здесь бизнес логика, в виде классов или методов.
# Сюда импортируются DAO классы из пакета dao и модели из dao.model
# Некоторые методы могут оказаться просто прослойкой между dao и views,
# но чаще всего будет какая-то логика обработки данных сейчас или в будущем.
import calendar
import datetime
import jwt
from flask_restx import abort
from flask import current_app
from project.exceptions import ItemNotFound
from project.services.users_service import UsersService
from project.tools.security import compose_passwords


class AuthService:
    def __init__(self, service: UsersService):
        self.service = service

    def generate_tokens(self, email: str, password: str, is_refresh=False) -> dict:
        user = self.service.get_by_email(email)
        if user is None:
            raise ItemNotFound(f'User with email={email} not exists.')

        if not is_refresh:
            if not compose_passwords(user.password, password):
                raise abort(400)

        data = {
            "email": user.email
        }

        # Создаем access_token на TOKEN_EXPIRE_MINUTES мин
        ttl_in_min = datetime.datetime.utcnow() + datetime.timedelta(minutes=current_app.config["TOKEN_EXPIRE_MINUTES"])
        data["exp"] = calendar.timegm(ttl_in_min.timetuple())
        access_token = jwt.encode(data, current_app.config["SECRET_KEY"], algorithm="HS256")

        # Создаем refresh_token на TOKEN_EXPIRE_DAYS дней
        ttl_in_days = datetime.datetime.utcnow() + datetime.timedelta(days=current_app.config["TOKEN_EXPIRE_DAYS"])
        data["exp"] = calendar.timegm(ttl_in_days.timetuple())
        refresh_token = jwt.encode(data, current_app.config["SECRET_KEY"], algorithm="HS256")

        return {
            "access_token": access_token,
            "refresh_token": refresh_token
        }

    def approve_refresh_token(self, refresh_token: str) -> dict:
        data = jwt.decode(jwt=refresh_token, key=current_app.config["SECRET_KEY"], algorithms=["HS256"])
        email = data.get("email")
        return self.generate_tokens(email, None, is_refresh=True)
