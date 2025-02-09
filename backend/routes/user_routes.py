from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.session import get_db
from services import user_services
from schemas.user_schema import *

# user_routes.py create a router object
#      import the necessary dependencies
#      import the db session
#      import the user_services
#      import the user schemas
#      create a router object
#      define the routes for the user endpoints
#      pass in the necessary parameters for the functions
#      return the response from the functions

router = APIRouter()

@router.post("/users/createNewUser")
def create_user(user: CreateNewUserSchema, db: Session = Depends(get_db)):
    return user_services.create_new_user(db, user.username, user.email, user.hashed_password)

@router.post("/users/updateUsername")
def update_username(user: UpdateUsernameSchema, db: Session = Depends(get_db)):
    return user_services.update_username(db, user.user_id, user.username)

@router.post("/users/updatePassword")
def update_password(user: UpdatePasswordSchema, db: Session = Depends(get_db)):
    return user_services.update_password(db, user.user_id, user.password)
