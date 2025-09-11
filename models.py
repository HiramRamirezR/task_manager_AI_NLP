from typing import Optional
from datetime import datetime
from sqlmodel import Field, SQLModel

class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    description: str
    due_date: datetime
    priority: str
    status: str