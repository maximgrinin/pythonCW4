# Здесь модель SQLAlchemy для сущности, также могут быть дополнительные методы работы с моделью
# (но не с базой, с базой мы работаем в классе DAO)
# from marshmallow import Schema, fields
from sqlalchemy import Column, String, Integer, Float
from project.setup.db.setup_db import db
from project.setup.db.base import Base
# from project.setup.db.genre import GenreSchema
# from project.setup.db.director import DirectorSchema


# Модель для фильмов
class Movie(Base):
    __tablename__ = 'movies'
    title = Column(String(255), unique=True, nullable=False)
    description = Column(String(255), nullable=False)
    trailer = Column(String(255), nullable=False)
    year = Column(Integer, nullable=False)
    rating = Column(Float, nullable=False)
    genre_id = Column(Integer, db.ForeignKey("genres.id"), nullable=False)
    genre = db.relationship("Genre")
    director_id = Column(Integer, db.ForeignKey("directors.id"), nullable=False)
    director = db.relationship("Director")


# # Схема для сериализации Фильма
# class MovieSchema(Schema):
#     id = fields.Int(dump_only=True)
#     title = fields.Str()
#     description = fields.Str()
#     trailer = fields.Str()
#     year = fields.Int()
#     rating = fields.Float()
#     genre = fields.Pluck(GenreSchema, 'name')
#     director = fields.Pluck(DirectorSchema, 'name')
