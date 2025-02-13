from pydantic import BaseModel
from datetime import datetime

class CreateNewTaskSchema(BaseModel):
    title: str
    description: str
    deadline: datetime
    urgency: str
    category: str
    importance: int

    completed: bool
    owner_id: int