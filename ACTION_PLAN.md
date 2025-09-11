# 🎯 Action Plan – AI Task Manager (MVP)

This will be a learning project, not a production project. The AI should act as a mentor, explaining and teaching concepts, reviewing the code I write, and correcting me if necessary, but should not write code for me directly. I will write every line, and the AI will only guide me.

---

### ✅ 1. Initial Project Setup

*Technologies: Python 3.10+, FastAPI, Uvicorn.*
**Goals:**
- ✅ Create a virtual environment.
- ✅ Install necessary dependencies.
- ✅ Set up the `main.py` entry point with a test endpoint (`/health`).

*Mentor: ✅ should explain the structure of a FastAPI project and why we use uvicorn as an ASGI server.*

---

### ✅ 2. Data Model and Basic CRUD

*Technologies: FastAPI, Pydantic.*
**Goals:**
- ✅ Define a `Task` model with fields: `id`, `description`, `due_date`, `priority`, `status`.
- ✅ Implement REST endpoints:
    - ✅ `POST /tasks` (create task).
    - ✅ `GET /tasks` (list all tasks).
    - ✅ `PUT /tasks/{id}` (update a task).
    - ✅ `DELETE /tasks/{id}` (delete task).

*Mentor: ✅ should teach the difference between input (request) and output (response) models in Pydantic, and explain how FastAPI automatically validates data.*

---

### ✅ 3. Data Persistence

*Technologies: SQLite + SQLModel (SQLAlchemy).*
**Goals:**
- ✅ Start with in-memory storage (`tasks_db` list).
- ✅ Connect a SQLite database using SQLModel and SQLAlchemy.

*Mentor: ✅ explain what a relational database is and why to use SQLite as an intermediate step for an MVP. Explain the Session pattern and dependency injection.*

---

### ✅ 4. NLP Endpoint for Creating Tasks from Natural Language

*Technologies: FastAPI, Pydantic, dateparser, regex.*
**Goals:**
- ✅ Create a `POST /tasks/nlp` endpoint that receives text.
- ✅ Implement robust logic to extract date and time.
- ✅ Implement the extraction of the task description.
- ✅ Build a complete `Task` object with the extracted data.
- ✅ Update the `Task` model so that `due_date` is of type `datetime`.
- ✅ Add the created task to the persistent database.

*Mentor: ✅ guide in the process of debugging, refactoring, and solution design. Explain concepts of immutability (`.replace()`), creating Pydantic objects, and the importance of a coherent data model.*

---

### ⏳ 5. Desktop User Interface (Phase 2)

*Technologies: PySide2 (Qt5), Requests.*
**Goals:**
- 🔲 Set up a basic Qt5 application window.
- 🔲 Design the main layout (task list, input fields, buttons).
- 🔲 Implement logic to fetch and display tasks from the API.
- 🔲 Implement functionality to create, update, and delete tasks by calling the API.
- 🔲 Connect the NLP input field to the `/tasks/nlp` endpoint.

*Mentor: guide on Qt basics like signals/slots, model/view architecture, and making HTTP requests.*
