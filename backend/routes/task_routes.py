from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.session import get_db
from services import task_services
from schemas.task_schema import *


# task_routes.py create a router object
#      import the necessary dependencies
#      import the db session
#      import the user_services
#      import the user schemas
#      create a router object
#      define the routes for the user endpoints
#      pass in the necessary parameters for the functions
#      return the response from the functions

router = APIRouter()

@router.post('/tasks/createNewTask')
def create_task(task: CreateNewTaskSchema, db: Session = Depends(get_db)):
    return task_services.create_new_task(db, task.title, task.description, task.deadline, task.urgency, task.category, task.importance, task.completed, task.owner_id)
