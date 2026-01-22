from sqlmodel import SQLModel, create_engine   #SQLModel is class that helps define tables and models
                                               #create_engine is a function to create a connection to database
sqlite_url = "sqlite:///expenses.db"           #sqlite is a simple file-based database
engine = create_engine(sqlite_url, echo = True)  

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)   