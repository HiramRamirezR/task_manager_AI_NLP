# Gestor de Tareas con AI (MVP)

Este es un proyecto de aprendizaje para construir una API de gestión de tareas usando FastAPI, con la guía de un mentor de IA.

## Estado Actual del Proyecto

El proyecto se encuentra en la fase inicial de desarrollo. Las siguientes funcionalidades están implementadas:

- **Configuración del Entorno**: Uso de un entorno virtual de Python (`.venv`).
- **Dependencias Principales**: `fastapi` y `uvicorn`.
- **Almacenamiento en Memoria**: Las tareas se guardan temporalmente en una lista en memoria.
- **Endpoints de la API**:
    - `GET /docs`: Documentación interactiva de la API.
    - `GET /health`: Endpoint para verificar el estado del servidor.
    - `GET /tasks`: Obtiene la lista de todas las tareas.
    - `POST /tasks`: Crea una nueva tarea.

## Próximos Pasos

El siguiente objetivo es implementar los endpoints `PUT` y `DELETE` para permitir la actualización y eliminación de tareas existentes.

## Cómo Ejecutar el Proyecto

1.  **Clonar el repositorio** (si aplica).

2.  **Crear y activar el entorno virtual**:
    ```bash
    # Crear el entorno
    python -m venv .venv

    # Activar en Windows (CMD)
    .venv\Scripts\activate

    # Activar en Windows (PowerShell)
    .\.venv\Scripts\Activate.ps1

    # Activar en Linux/macOS (Bash)
    source .venv/bin/activate
    ```

3.  **Instalar las dependencias**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Iniciar el servidor de desarrollo**:
    ```bash
    uvicorn main:app --reload
    ```

5.  **Acceder a la API**:
    - La API estará disponible en `http://127.0.0.1:8000`.
    - La documentación interactiva se encuentra en `http://127.0.0.1:8000/docs`.
