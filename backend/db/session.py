# for a db connection we need to create an engine and a session maker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#Set the URL for the database to identify where the database is located
DB_URL = "postgresql://postgres:password@localhost:5432/postgres"    

# set engine to create pipeline to the database
db_engine = create_engine(DB_URL)
# use engine to create a session maker which will be used to create a session to interact with the database
db_session = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)

#create a function to get a session using the session maker
def get_db():
    db = db_session()
    try:
        yield db
    finally:
        db.close()