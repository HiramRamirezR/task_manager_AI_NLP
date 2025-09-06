from fastapi import FastAPI, HTTPException
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

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_update: Task):
    for i, task in enumerate(tasks_db):
        if task.id == task_id:
            task_update.id = task_id
            tasks_db[i] = task_update
            return task_update
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for i, task in enumerate(tasks_db):
        if task.id == task_id:
            del tasks_db[i]
            return {"status": "success", "message": "Task deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")
