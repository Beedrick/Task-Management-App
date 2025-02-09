from pydantic import BaseModel
from datetime import datetime

class CreateNewTaskSchema(BaseModel):
    title: str
    description: str
    progress: str
    priority: str
    category: str
    due_date: datetime
    completed: bool
    owner_id: int