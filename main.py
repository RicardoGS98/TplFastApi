"""
Incluir las rutas aqui.

from fastapi import FastAPI

from app.api.v1.routes import *

app = FastAPI()

app.include_router(user.router, prefix="/api/v1")
"""
