from flask import request
from flask_restx import Namespace, Resource, abort
import jwt
from flask import current_app
from project.container import user_service
# from project.setup.api.models import user
from project.setup.db.user import UserSchema

user_ns = Namespace('user')

# Создаем экземпляры схем сериализации для одной и нескольких сущностей
user_schema = UserSchema()
users_schema = UserSchema(many=True)


# Декоратор для проверки авторизации
def auth_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)
        data = request.headers['Authorization']
        token = data.split("Bearer ")[-1]
        try:
            result = jwt.decode(token, key=current_app.config["SECRET_KEY"], algorithms=["HS256"])
            email = result.get('email')
            kwargs["email"] = email
        except Exception as e:
            print("JWT Decode Exсeption", e)
            abort(401)

        return func(*args, **kwargs)

    return wrapper


# Функции API для пользователей - /user/
# - **GET** /user/ — получить информацию о пользователе (его профиль).
# - **PATCH** /user/ — изменить информацию пользователя (имя, фамилия, любимый жанр).
@user_ns.route('/')
class UserView(Resource):
    @auth_required
    # @user_ns.marshal_with(user, code=200, description='OK')
    def get(self, email=None):
        return user_schema.dump(user_service.get_by_email(email))
        # return user_service.get_by_email(email)

    @auth_required
    def patch(self, email=None):
        try:
            req_json = request.json
            user_service.update(email, req_json)
            return "", 204
        except Exception as e:
            return f'Ошибка при обновлении данных: {str(e)}', 404


# Функции API для пользователей - /user/
# - **PUT** /user/password — обновить пароль пользователя, для этого нужно отправить два пароля *old_password* и new_password*.*
@user_ns.route('/password/')
class UsersPasswordView(Resource):
    @auth_required
    def put(self, email=None):
        req_json = request.json
        if not req_json:
            return 'Ошибка при получении информации при смене пароля', 404

        old_password = req_json.get('old_password', None)
        new_password = req_json.get('new_password', None)
        if None in [old_password, new_password]:
            return '', 400

        try:
            user_service.password_update(email, req_json)
            return "", 204
        except Exception as e:
            return f'Ошибка при обновлении пароля: {str(e)}', 404
