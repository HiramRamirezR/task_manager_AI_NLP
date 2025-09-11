# AI-Powered Task Manager (MVP)

This is a learning project to build a task management API using FastAPI, with guidance from an AI mentor. The project features a complete CRUD API, data persistence with SQLite, and a Natural Language Processing endpoint for task creation.

## Features

- **FastAPI Backend**: A modern, fast (high-performance) web framework for building APIs.
- **SQLite Database**: Persistent data storage using SQLite, managed with SQLModel and SQLAlchemy.
- **Full CRUD Functionality**: All standard Create, Read, Update, and Delete operations for tasks are implemented.
- **Natural Language Task Creation**: A special endpoint at `/tasks/nlp` that accepts a sentence in natural language (Spanish or English) and automatically parses the description and due date to create a task.
- **Interactive API Docs**: Automatic, interactive API documentation provided by FastAPI at `/docs`.

## How to Run the Project

1.  **Clone the repository** (if applicable).

2.  **Create and activate a virtual environment**:
    ```bash
    # Create the environment
    python -m venv .venv

    # Activate on Windows (Command Prompt)
    .venv\Scripts\activate

    # Activate on Windows (PowerShell)
    .\.venv\.Scripts\Activate.ps1

    # Activate on Linux/macOS (Bash)
    source .venv/bin/activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Start the development server**:
    The application uses `uvicorn` to run. The `--reload` flag enables hot-reloading on code changes.
    ```bash
    uvicorn main:app --reload
    ```
    When you run this command for the first time, it will create a `database.db` file for the SQLite database.

5.  **Access the API**:
    - The API will be available at `http://127.0.0.1:8000`.
    - The interactive documentation can be accessed at `http://127.0.0.1:8000/docs`.

## API Endpoints

- `GET /tasks`: Retrieve all tasks.
- `POST /tasks`: Create a new task.
- `PUT /tasks/{task_id}`: Update an existing task.
- `DELETE /tasks/{task_id}`: Delete a task.
- `POST /tasks/nlp`: Create a new task from a natural language query.
- `GET /health`: Health check endpoint.