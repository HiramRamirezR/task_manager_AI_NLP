from fastapi import FastAPI, HTTPException
from datetime import date, datetime
from pydantic import BaseModel
import re
from dateparser.search import search_dates

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

class NlpRequest(BaseModel):
    text: str

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

@app.post("/tasks/nlp")
def create_task_from_nlp(request: NlpRequest):
    text = request.text

    time_pattern = r'\b(?:a las|a la|a eso de las)?\s*(\d{1,2})(?::(\d{2}))?\s*(am|pm)?\b'
    time_match = re.search(time_pattern, text, re.IGNORECASE)

    time_is_present_in_text = time_match is not None

    settings = {'PREFER_DATES_FROM': 'future'}
    found_dates = search_dates(
        text,
        languages=["es", "en"],
        settings=settings)


    date_text_found = None
    due_date = None

    if found_dates:
        date_text_found = found_dates[0][0]
        due_date = found_dates[0][1]

        description = text.replace(date_text_found, "").strip()

        if not time_is_present_in_text:
            due_date = due_date.replace(hour=0, minute=0, second=0, microsecond=0)

    if not due_date:
        raise HTTPException(status_code=400, detail="No date found in text")

    return {
        "original_text": text,
        "date_text_found": date_text_found,
        "parsed_date": due_date,
        "description": description,
        "year": due_date.year,
        "month": due_date.month,
        "day": due_date.day,
        "hour": due_date.hour,
        "minute": due_date.minute
    }

# Result

"""{
  "original_text": "revisar el informe mañana a las 5pm",
  "date_text_found": "mañana a las 5pm",
  "parsed_date": "2025-09-11T17:00:00",
  "description": "revisar el informe",
  "year": 2025,
  "month": 9,
  "day": 11,
  "hour": 17,
  "minute": 0
}"""