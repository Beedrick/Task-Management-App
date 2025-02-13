from db.models import Task, User
from sqlalchemy.orm import Session
from datetime import datetime

def create_new_task(db: Session, title: str, description: str, 
                    progress: int, priority: int, category: str, 
                    due_date: datetime, owner_id: int):
    task = Task(title=title, description=description, progress=progress,
                priority=priority, category=category, due_date=due_date,
                owner_id=owner_id, username = db.query(User).filter(User.id == owner_id).first().username)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def delete_task(db: Session, task_id: int):
    db.query(Task).filter(Task.id == task_id).delete()
    db.commit()
    return {"message": "Task deleted"}


    