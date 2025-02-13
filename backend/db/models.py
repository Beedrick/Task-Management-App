from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    
    # Define a relationship to the Task class
    tasks = relationship("Task", back_populates="owner")

class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    title = Column(String)
    description = Column(String)
    deadline = Column(DateTime)
    urgency = Column(String)  # High, Medium, Low
    category = Column(String) # Work, Personal, Study, etc.
    importance = Column(Integer) # 1 to 10

    completed = Column(Boolean)
    owner_id = Column(Integer, ForeignKey('users.id'))  # Foreign key to User.id
    username = Column(String) # The user who created the task

    # Define a relationship to the User class
    owner = relationship("User", back_populates="tasks")