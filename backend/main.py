from fastapi import FastAPI
from db.models import Base
from db.session import db_engine
from routes import user_routes, task_routes


app = FastAPI()

Base.metadata.create_all(bind=db_engine)

app.include_router(user_routes.router)
app.include_router(task_routes.router)

@app.get("/")
def say_hello():
    return {"Hello": "World"}

