from flask_restx import fields, Model
from project.setup.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})

director: Model = api.model('Режиссер', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Люк Бессон'),
})

movie: Model = api.model('Фильм', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True, max_length=255, example='Крепкий орешек'),
    'description': fields.String(required=True, max_length=255, example='Фильм о том, как провести рождество с пользой'),
    'trailer': fields.String(required=True, max_length=255, example='https://www.youtube.com/'),
    'year': fields.Integer(required=True, example=1981),
    'rating': fields.Float(required=True, example=8.1),
    'genre_id': fields.Integer(required=True, example=1),
    'director_id': fields.Integer(required=True, example=1),
})

user: Model = api.model('Пользователь', {
    'id': fields.Integer(required=True, example=1),
    'email': fields.String(required=True, max_length=255, example='address@domain.com'),
    'name': fields.String(max_length=255, example='Майк'),
    'surname': fields.String(max_length=255, example='Вазовски'),
    'favourite_genre': fields.Integer(example=1),
})

favorites: Model = api.model('Избранное', {
    'user_id': fields.Integer(required=True, example=1),
    'movie_id': fields.Integer(required=True, example=1),
})
