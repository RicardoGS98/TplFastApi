# FastAPI Base Project

This project serves as a base template for quickly developing APIs with FastAPI. It includes essential configurations and structures for managing models, schemas, and services.

## Features

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.6+.
- **SQLAlchemy**: SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- **Pydantic**: Data validation and settings management using Python type annotations.
- **Alembic**: Lightweight database migration tool for use with SQLAlchemy.

## Project Structure

- `app/api/v1/services/`: Contains service functions to interact with the database and apply business logic.
- `app/models/`: Contains SQLAlchemy models.
- `app/schemas/`: Contains Pydantic schemas for data validation and serialization.

## Getting Started

### Prerequisites

- Python 3.6+
- pip (Python package installer)

### Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

### Database Setup

1. Initialize the database:
    ```sh
    alembic revision --autogenerate -m "Initial migration"
    alembic upgrade head
    ```

### Running the Application

1. Start the FastAPI server:
    ```sh
    uvicorn app.main:app --reload
    ```


## Example Usage

### Creating a User

1. Define the user model in `app/models/user.py`:
    ```python
    from sqlalchemy import Column, Integer, String
    from app.core.base import Base

    class User(Base):
        __tablename__ = 'users'
        id = Column(Integer, primary_key=True, index=True)
        name = Column(String, index=True)
        email = Column(String, unique=True, index=True)
        age = Column(Integer)
    ```

2. Define the user schema in `app/schemas/user.py`:
    ```python
    from pydantic import BaseModel

    class UserCreate(BaseModel):
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
    ```

3. Define the user service in `app/api/v1/services/user.py`:
    ```python
    from sqlalchemy.orm import Session
    from app.models.user import User
    from app.schemas.user import UserCreate

    def create_user(db: Session, user: UserCreate):
        db_user = User(**user.dict())
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    def get_user(db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first()
    ```

## License

This project is licensed under the MIT License.