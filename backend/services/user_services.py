from sqlalchemy.orm import Session
from db.models import User

# User_services.py create functions to interact with db for users table
# CRUD operations for users table in your postgres db
#       define function and pass in db session
#       pass in the parameters needed for that function
#       use the User model and the db session to operate on the db creating, reading, updating, and deleting users
#       return the user object or a message to the user

def create_new_user(db: Session, username: str, email: str, password: str):
    user = User(username=username, email=email, hashed_password=password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def update_username(db: Session, user_id: int, username: str):
    # this line queries the db for the user with the id that matches the user_id passed in
    user = db.query(User).filter(User.id == user_id).first()
    # this line updates the username of the user with the username passed in
    user.username = username
    # this line commits the changes to the db
    db.commit()
    # this line refreshes the user object to reflect the changes made
    db.refresh(user)
    # this line returns the user object
    return user

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_users(db: Session):
    return db.query(User).all()

def delete_user(db: Session, user_id: int):
    db.query(User).filter(User.id == user_id).delete()
    db.commit()
    return {"message": "User deleted"}

def update_email(db: Session, user_id: int, email: str):
    user = db.query(User).filter(User.id == user_id).first()
    user.email = email
    db.commit()
    db.refresh(user)
    return user

def update_password(db: Session, user_id: int, password: str):
    user = db.query(User).filter(User.id == user_id).first()
    user.hashed_password = password
    db.commit()
    db.refresh(user)
    return user