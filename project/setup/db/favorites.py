# Здесь модель SQLAlchemy для сущности, также могут быть дополнительные методы работы с моделью
# (но не с базой, с базой мы работаем в классе DAO)
from sqlalchemy import Column, Integer
from project.setup.db.setup_db import db
from project.setup.db.base import Base


# Модель для фильмов
class Favorites(Base):
    __tablename__ = 'favorites'
    user_id = Column(Integer, db.ForeignKey("users.id"), nullable=False)
    user = db.relationship("User")
    movie_id = Column(Integer, db.ForeignKey("movies.id"), nullable=False)
    movie = db.relationship("Movie")
