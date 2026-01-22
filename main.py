from fastapi import FastAPI
from database import create_db_and_tables

app = FastAPI()

@app.get('/')
def root():
    return {'status' : 'server is up and running'}

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

