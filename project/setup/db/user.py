# Здесь модель SQLAlchemy для сущности, также могут быть дополнительные методы работы с моделью
# (но не с базой, с базой мы работаем в классе DAO)
from marshmallow import Schema, fields
from sqlalchemy import Column, String, Integer
from project.setup.db.base import Base
# from project.setup.db.genre import GenreSchema
from project.setup.db.setup_db import db


# Модель для Пользователя
class User(Base):
    __tablename__ = 'users'
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    name = Column(String(255))
    surname = Column(String(255))
    favourite_genre = Column(Integer, db.ForeignKey("genres.id"))
    genre = db.relationship("Genre")


# Схема для сериализации Пользователя
class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Str()
    name = fields.Str()
    surname = fields.Str()
    favourite_genre = fields.Int()
    # favourite_genre = fields.Nested(GenreSchema)
    # genre = fields.Nested(GenreSchema)
