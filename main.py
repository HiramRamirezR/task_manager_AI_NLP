from fastapi import FastAPI
from datetime import date
from pydantic import BaseModel

app = FastAPI()
tasks_db = []

@app.get("/health")
def health_check():
    return {"status": "ok"}

class Task(BaseModel):
    id: int
    description: str
    due_date: date
    priority: str
    status: str

@app.get("/tasks", response_model=list[Task])
def get_all_tasks():
    return tasks_db

@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    tasks_db.append(task)
    return task