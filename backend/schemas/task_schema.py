from pydantic import BaseModel

class TaskSchema(BaseModel):
    title: str
    description: str
    progress: str
    priority: str
    category: str
    due_date: str
    completed: bool
    owner_id: int
    id: int