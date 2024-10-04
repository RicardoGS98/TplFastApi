"""
Colocar aquí todas las rutas de la aplicación.
Ejemplo:
# user.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.session import get_db
from app.core.security import verify_api_token
from app.schemas.user import UserCreate, UserResponse
from app.services.user import create_user

router = APIRouter()

@router.post("/user/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db), api_key: str = Depends(verify_api_token)):
    try:
        db_user = create_user(db, user)
        return db_user
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error creating user: {str(e)}")

"""