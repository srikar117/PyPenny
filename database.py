from sqlmodel import SQLModel, create_engine

sqlite_url = "sqlite:///expenses.db"
engine = create_engine(sqlite_url, echo = True)

def create_db_tables():
    SQLModel.metadata.create_all(engine)