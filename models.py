from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import date

class Category(SQLModel, table = True):
    id: Optional[int] = Field(default = None, primary_key = True)
    name : str

class Expense(SQLModel, table = True):
    id: Optional[int] = Field(default = None, primary_key = True)
    amount : float
    description : Optional[str] = None
    date : date = Field(default_factory = date.today)
    category_id : Optional[int] = Field(default = None, foreign_key = 'category.id')    