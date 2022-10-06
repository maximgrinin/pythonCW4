from flask import request
from flask_restx import Namespace, Resource
from project.container import auth_service, user_service

auth_ns = Namespace('auth')


@auth_ns.route('/register/')
class AuthRegisterView(Resource):
    @auth_ns.response(404, 'Not Found')
    def post(self):
        req_json = request.json
        if not req_json:
            return 'Ошибка при получении информации о новом пользователе', 404
        user_service.create(req_json)
        return "", 201


# Функции API для авторизации
@auth_ns.route('/login/')
class AuthLoginView(Resource):
    @auth_ns.response(404, 'Not Found')
    def post(self):
        req_json = request.json
        if not req_json:
            return 'Ошибка при получении информации при авторизации', 404

        email = req_json.get('email', None)
        password = req_json.get('password', None)
        if None in [email, password]:
            return '', 400

        tokens = auth_service.generate_tokens(email, password)
        return tokens, 201

    def put(self):
        req_json = request.json
        token = req_json.get("refresh_token")
        try:
            tokens = auth_service.approve_refresh_token(token)
            return tokens, 201
        except Exception as e:
            return f'Ошибка авторизации, {str(e)}', 401
