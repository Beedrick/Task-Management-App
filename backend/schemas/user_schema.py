from pydantic import BaseModel

class CreateNewUserSchema(BaseModel):
    username: str
    email: str
    hashed_password: str

class UpdateUsernameSchema(BaseModel):
    username: str
    user_id: int

class UpdatePasswordSchema(BaseModel):
    password: str
    user_id: int

