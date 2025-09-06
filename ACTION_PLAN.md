# 🎯 Plan de Acción – Gestor de Tareas con AI (MVP)

Este será un proyecto de aprendizaje, no un proyecto de producción.
La IA debe actuar como mentor, explicando y enseñando los conceptos, revisando el código que yo escriba y corrigiéndome si es necesario, pero no debe escribir código por mí directamente. Yo escribiré cada línea, y la IA solo me guiará.

---

### ✅ 1. Configuración inicial del proyecto

*Tecnologías: Python 3.10+, FastAPI, Uvicorn.*
**Objetivos:**
- ✅ Crear un entorno virtual.
- ✅ Instalar dependencias necesarias.
- ✅ Configurar el punto de entrada `main.py` con un endpoint de prueba (`/health`).

*Mentor: ✅ debe explicar la estructura de un proyecto FastAPI y por qué usamos uvicorn como servidor ASGI.*

---

### ⏳ 2. Modelo de datos y CRUD básico

*Tecnologías: FastAPI, Pydantic.*
**Objetivos:**
- ✅ Definir un modelo `Task` con campos: `id`, `description`, `due_date`, `priority`, `status`.
- Implementar endpoints REST:
    - ✅ `POST /tasks` (crear tarea).
    - ✅ `GET /tasks` (listar todas las tareas).
    - ➡️ `PUT /tasks/{id}` (actualizar una tarea).
    - `DELETE /tasks/{id}` (eliminar tarea).

*Mentor: ✅ debe enseñar la diferencia entre modelos de entrada (request) y salida (response) en Pydantic, y explicar cómo FastAPI valida automáticamente los datos.*

---

### ⏳ 3. Persistencia de datos

*Tecnologías: SQLite + SQLAlchemy (opcional, se puede usar una lista en memoria primero).*
**Objetivos:**
- ✅ Empezar con almacenamiento en memoria (lista `tasks_db`).
- Opcionalmente, conectar una base SQLite usando SQLAlchemy.

*Mentor: explicar qué es una base de datos relacional y por qué usar SQLite como paso intermedio para un MVP.*

---

### 4. Endpoint de NLP para crear tareas desde lenguaje natural

*Tecnologías: spaCy (o regex + heurísticas si queremos algo más simple).*
**Objetivos:**
- Crear un endpoint `POST /tasks/nlp` que reciba frases como:
    - “Recuérdame enviar el reporte el lunes a las 9 am con prioridad alta”.
- Parsear la frase y devolver una tarea estructurada.