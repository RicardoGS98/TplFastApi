"""
Aquí colocar las definiciones pydantic de los esquemas de los modelos de la base de datos
asi como la validacion de los mismos.
Ejemplo:
# user.py
from pydantic import BaseModel
class UserCreate(BaseModel):
    id: int
    name: str
    email: str
    age: int

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    age: int
    class Config:
        orm_mode = True
"""
