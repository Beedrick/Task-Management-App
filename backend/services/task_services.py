from db.session import get_db
from db.models import Task

db = get_db()

def create_new_task(title: str, description: str, progress: str, priority: str, category: str, due_date: datetime, owner_id: int):
    task = Task(title=title, description=description, progress=progress, priority=priority, category=category, due_date=due_date, owner_id=owner_id)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def get_task_by_id(task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()

def get_tasks():
    return db.query(Task).all()

def delete_task(task_id: int):
    db.query(Task).filter(Task.id == task_id).delete()
    db.commit()
    return {"message": "Task deleted"}

def update_task_title(task_id: int, title: str):
    task = db.query(Task).filter(Task.id == task_id).first()
    task.title = title
    db.commit()
    db.refresh(task)
    return task

def update_task_description(task_id: int, description: str):
    task = db.query(Task).filter(Task.id == task_id).first()
    task.description = description
    db.commit()
    db.refresh(task)
    return task

def update_task_progress(task_id: int, progress: str):
    task = db.query(Task).filter(Task.id == task_id).first()
    task.progress = progress
    db.commit()
    db.refresh(task)
    return task

def update_task_priority(task_id: int, priority: str):
    task = db.query(Task).filter(Task.id == task_id).first()
    task.priority = priority
    db.commit()
    db.refresh(task)
    return task

def update_task_category(task_id: int, category: str):
    task = db.query(Task).filter(Task.id == task_id).first()
    task.category = category
    db.commit()
    db.refresh(task)
    return task

def update_task_due_date(task_id: int, due_date: datetime):
    task = db.query(Task).filter(Task.id == task_id).first()
    task.due_date = due_date
    db.commit()
    db.refresh(task)
    return task

def update_task_completed(task_id: int, completed: bool):
    task = db.query(Task).filter(Task.id == task_id).first()
    task.completed = completed
    db.commit()
    db.refresh(task)
    return task

