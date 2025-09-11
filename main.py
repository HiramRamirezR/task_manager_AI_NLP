from fastapi import FastAPI, HTTPException, Depends
from datetime import date, datetime
from pydantic import BaseModel
import re
from dateparser.search import search_dates
from models import Task
from database import engine
from sqlmodel import SQLModel, Session, select

app = FastAPI()

# This function create the table in the DB
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


# Function to obtain a data base session
def get_session():
    with Session(engine) as session:
        yield session


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/health")
def health_check():
    return {"status": "ok"}


class NlpRequest(BaseModel):
    text: str

@app.get("/tasks", response_model=list[Task])
def get_all_tasks(session: Session = Depends(get_session)):
    tasks = session.exec(select(Task)).all()
    return tasks


@app.post("/tasks", response_model=Task)
def create_task(task: Task, session: Session = Depends(get_session)):
    session.add(task)
    session.commit()
    session.refresh(task)
    return task


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_update: Task, session: Session = Depends(get_session)):
    db_task = session.get(Task, task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")

    update_data = task_update.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_task, key, value)

    session.add(db_task)
    session.commit()
    session.refresh(db_task)

    return db_task


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int, session: Session = Depends(get_session)):
    db_task = session.get(Task, task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")

    session.delete(db_task)
    session.commit()


@app.post("/tasks/nlp", response_model=Task)
def create_task_from_nlp(request: NlpRequest, session: Session = Depends(get_session)):
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

        priority = "Urgente"
        status = "Pendiente"

        if not time_is_present_in_text:
            due_date = due_date.replace(hour=0, minute=0, second=0, microsecond=0)

        new_task = Task(
            description=description,
            due_date=due_date,
            priority=priority,
            status=status
        )

        session.add(new_task)
        session.commit()
        session.refresh(new_task)

        return new_task

    if not due_date:
        raise HTTPException(status_code=400, detail="No date found in text")

# Response body

"""{
  "id": 1,
  "description": "revisar el informe",
  "due_date": "2025-09-11T17:00:00",
  "priority": "Urgente",
  "status": "Pendiente"
}"""