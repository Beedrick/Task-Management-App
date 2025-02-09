from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.session import get_db
from services import user_services

router = APIRouter()

@router.post("/users/")
def create_user(username: str, email: str, password: str, db: Session = Depends(get_db)):
    return user_services.create_new_user(db, username, email, password)

