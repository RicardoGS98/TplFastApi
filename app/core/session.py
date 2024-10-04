"""
Contiene la configuracion de conexion a DB
"""

import logging
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

USERNAME = os.environ.get('DB_USERNAME')
PASSWORD = os.environ.get('DB_PASSWORD')
PORT = os.environ.get('DB_PORT')
DATABASE = os.environ.get('DB_NAME')


# Configuración básica para el entorno de desarrollo
class Config:
    ECHO = False
    DATABASE_URI = f'postgresql+psycopg2://{USERNAME}:{PASSWORD}@db:5432/{DATABASE}?'
    LOG_LVL = logging.DEBUG


# Configuración para el entorno de producción
class ProductionConfig(Config):
    LOG_LVL = logging.INFO


# Configuración para el entorno de desarrollo
class DevelopmentConfig(Config):
    ECHO = True


# Selecciona la configuración apropiada basándote en la variable de entorno del sistema
config = {
    "local": DevelopmentConfig,
    "production": ProductionConfig
}
app_config: Config = config[os.environ.get('ENVIRONMENT')]

engine = create_engine(app_config.DATABASE_URI, echo=app_config.ECHO)

logging.basicConfig(level=app_config.LOG_LVL, format='%(asctime)s - %(levelname)s - %(message)s')

Session = sessionmaker(bind=engine)


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
