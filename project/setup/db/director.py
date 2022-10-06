# Здесь модель SQLAlchemy для сущности, также могут быть дополнительные методы работы с моделью
# (но не с базой, с базой мы работаем в классе DAO)
# from marshmallow import Schema, fields
from sqlalchemy import Column, String
from project.setup.db.base import Base


# Модель для режиссеров
class Director(Base):
    __tablename__ = 'directors'
    name = Column(String(255), unique=True, nullable=False)


# # Схема для сериализации Режиссера
# class DirectorSchema(Schema):
#     id = fields.Int(dump_only=True)
#     name = fields.Str()
