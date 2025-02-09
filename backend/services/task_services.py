from db.models import Task, User
from sqlalchemy.orm import Session
from datetime import datetime

def create_new_task(db: Session, title: str, description: str, 
                    progress: int, priority: int, category: str, 
                    due_date: datetime, owner_id: int):
    task = Task(title=title, description=description, progress=progress,
                priority=priority, category=category, due_date=due_date,
                owner_id=owner_id)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

