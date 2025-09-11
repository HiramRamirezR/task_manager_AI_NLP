# AI-Powered Task Manager

A desktop task management application built with Python, featuring a powerful FastAPI backend and a user-friendly Qt5 interface. The application leverages Natural Language Processing for intelligent task creation.

## Architecture

This project follows a modern client-server architecture:

- **Backend**: A REST API built with **FastAPI** that handles all business logic, data persistence (via **SQLModel** and **SQLite**), and Natural Language Processing.
- **Frontend**: A desktop client built with **PySide2 (Qt5)** that provides the user interface and communicates with the backend via HTTP requests.

## Features

- **Intuitive Desktop UI**: A clean and simple user interface built with Qt5.
- **Persistent Task Storage**: Tasks are saved in a local SQLite database.
- **Full CRUD Functionality**: Create, Read, Update, and Delete tasks through the UI.
- **Natural Language Task Creation**: A special input field to create tasks from simple sentences (e.g., "review report tomorrow at 5pm").
- **Decoupled Architecture**: A professional separation of the frontend client and the backend server.

## How to Run the Project

This project has two components that need to be run separately: the **Backend API** and the **Desktop UI**.

### 1. Setup

1.  **Clone the repository** (if applicable).
2.  **Create and activate a virtual environment**:
    ```bash
    python -m venv .venv
    .venv\Scripts\activate
    ```
3.  **Install dependencies**:
    This will install dependencies for both the backend and the UI.
    ```bash
    pip install -r requirements.txt
    ```

### 2. Running the Application

1.  **Start the Backend API**:
    Open a terminal, activate the virtual environment, and run:
    ```bash
    uvicorn main:app --reload
    ```
    Leave this terminal running. The API is now available at `http://127.0.0.1:8000`.

2.  **Launch the Desktop UI**:
    Open a **second terminal**, activate the same virtual environment, and run:
    ```bash
    python ui_main.py 
    ```
    *(Note: We will create the `ui_main.py` file in the next steps).*

## API Documentation

While using the desktop app, you can still access the backend's interactive documentation by navigating to `http://127.0.0.1:8000/docs` in your web browser.
