from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    
    # Define a relationship to the Task class
    tasks = relationship("Task", back_populates="owner")

class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    progress = Column(String)
    priority = Column(String)
    category = Column(String)
    due_date = Column(DateTime)
    completed = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey('users.id'))  # Foreign key to User.id
    
    # Define a relationship to the User class
    owner = relationship("User", back_populates="tasks")