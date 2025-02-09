from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.session import get_db
from services import user_services
from schemas.user_schema import UserSchema
from db.models import User

router = APIRouter()

@router.post("/users/")
def create_user(user: UserSchema, db: Session = Depends(get_db)):
    return user_services.create_new_user(db, user.username, user.email, user.hashed_password)

