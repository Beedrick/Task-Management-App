from db.models import Task, User
from sqlalchemy.orm import Session
from datetime import datetime

def create_new_task(db: Session, title: str, description: str, 
                    deadline: datetime, urgency: str, category: str, 
                    importance: int, completed: bool, 
                    owner_id: int):
    
    task = Task(title=title, description=description, deadline=deadline,
                urgency=urgency, category=category, 
                importance=importance, completed=completed, owner_id=owner_id,
                username = db.query(User).filter(User.id == owner_id).first().username)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def delete_task(db: Session, task_id: int):
    db.query(Task).filter(Task.id == task_id).delete()
    db.commit()
    return {"message": "Task deleted"}

def get_user_tasks(db: Session, user_id: int):
    return db.query(Task).filter(Task.owner_id == user_id).all()

    