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

### ✅ 2. Modelo de datos y CRUD básico

*Tecnologías: FastAPI, Pydantic.*
**Objetivos:**
- ✅ Definir un modelo `Task` con campos: `id`, `description`, `due_date`, `priority`, `status`.
- Implementar endpoints REST:
    - ✅ `POST /tasks` (crear tarea).
    - ✅ `GET /tasks` (listar todas las tareas).
    - ✅ `PUT /tasks/{id}` (actualizar una tarea).
    - ✅ `DELETE /tasks/{id}` (eliminar tarea).

*Mentor: ✅ debe enseñar la diferencia entre modelos de entrada (request) y salida (response) en Pydantic, y explicar cómo FastAPI valida automáticamente los datos.*

---

### ⏳ 3. Persistencia de datos

*Tecnologías: SQLite + SQLAlchemy (opcional, se puede usar una lista en memoria primero).*
**Objetivos:**
- ✅ Empezar con almacenamiento en memoria (lista `tasks_db`).
- Opcionalmente, conectar una base SQLite usando SQLAlchemy.

*Mentor: explicar qué es una base de datos relacional y por qué usar SQLite como paso intermedio para un MVP.*

---

### ✅ 4. Endpoint de NLP para crear tareas desde lenguaje natural

*Tecnologías: FastAPI, Pydantic, dateparser, regex.*
**Objetivos:**
- ✅ Crear un endpoint `POST /tasks/nlp` que recibe texto.
- ✅ Implementar una lógica robusta para extraer fecha y hora, solucionando las limitaciones de `dateparser` con una estrategia híbrida.
- ✅ Implementar la extracción de la descripción de la tarea del texto original.
- ✅ Construir un objeto `Task` completo con los datos extraídos y valores por defecto.
- ✅ Actualizar el modelo `Task` para que `due_date` sea de tipo `datetime` y pueda almacenar la hora.
- ✅ Añadir la tarea creada a la base de datos en memoria.

*Mentor: ✅ guiar en el proceso de depuración, refactorización, y diseño de la solución. Explicar conceptos de inmutabilidad (`.replace()`), creación de objetos Pydantic, y la importancia de un modelo de datos coherente.*