from fastapi import APIRouter, Depends
from services import ai_services
from sqlalchemy.orm import Session
from db.session import get_db
from db.models import Task
from schemas.ai_schema import *

router = APIRouter()

@router.post('/ai/autoPrioritizeTasks')
def auto_prioritize_tasks(user: PrioritizeTasksSchema, db: Session = Depends(get_db)):
    
    tasks = db.query(Task).filter(Task.owner_id == user.owner_id).all()
    
    return ai_services.auto_prioritize_tasks(tasks)