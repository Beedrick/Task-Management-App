from pydantic import BaseModel

class PrioritizeTasksSchema(BaseModel):
    owner_id: int