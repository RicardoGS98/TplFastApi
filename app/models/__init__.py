"""
Colocar aquí todos los modelos de la aplicación.
Para generar los cambios en la base de datos, se debe ejecutar el comando:
$ alembic revision --autogenerate -m "Nombre de la migración"
$ alembic upgrade head
Ejemplo:
# user.py
from sqlalchemy import Column, Integer, String
from app.core.base import Base
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    age = Column(Integer)
"""