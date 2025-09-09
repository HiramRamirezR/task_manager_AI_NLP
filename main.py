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

    settings = {'PREFER_DATES_FROM': 'future'}

    found_dates = search_dates(
        text,
        languages=["es", "en"],
        settings=settings)

    time_pattern = r'\b(?:a las|a la|a eso de las)?\s*(\d{1,2})(?::(\d{2}))?\s*(am|pm)?\b'
    time_match = re.search(time_pattern, text, re.IGNORECASE)

    date_text_found = None
    due_date = None

    if found_dates:
        date_text_found = found_dates[0][0]
        due_date = found_dates[0][1]

        if time_match:
            hour = int(time_match.group(1))
            minute = int(time_match.group(2)) if time_match.group(2) else 0
            am_pm = time_match.group(3)

            if am_pm and am_pm.lower() == "pm" and hour < 12:
                hour += 12
            elif am_pm and am_pm.lower() == "am" and hour == 12:
                hour = 0

            due_date = datetime(
                due_date.year,
                due_date.month,
                due_date.day,
                hour,
                minute
            )

    return {
        "original_text": text,
        "date_text_found": date_text_found,
        "parsed_date": due_date,
        "year": due_date.year,
        "month": due_date.month,
        "day": due_date.day,
        "hour": hour,
        "minute": minute
    }

# resutl

# {
#   "original_text": "enviar informe manana a las 9",
#   "date_text_found": "manana a las 9",
#   "parsed_date": "2025-09-10T09:00:00",
#   "year": 2025,
#   "month": 9,
#   "day": 10,
#   "hour": 9,
#   "minute": 0
# }

"""
{
  "original_text": "reunion el 15 de octubre a las 10:30 am",
  "date_text_found": "15 de octubre a las 10:30 am",
  "parsed_date": "2025-10-15T15:00:00",
  "year": 2025,
  "month": 10,
  "day": 15,
  "hour": 15,
  "minute": 0
}"""

# Internal Server Error