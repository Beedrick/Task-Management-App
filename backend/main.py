from fastapi import FastAPI
from db.models import Base
from db.session import db_engine
from routes import users


app = FastAPI()

Base.metadata.create_all(bind=db_engine)

app.include_router(users.router, prefix="/users")

@app.get("/")
def say_hello():
    return {"Hello": "World"}

