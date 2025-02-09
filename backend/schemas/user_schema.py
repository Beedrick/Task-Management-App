from pydantic import BaseModel

class UserSchema(BaseModel):
    username: str
    email: str
    id: int
    hashed_password: str
