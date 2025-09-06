Ì≥å Plan de Acci√≥n ‚Äì Gestor de Tareas con AI (MVP)

Este ser√° un proyecto de aprendizaje, no un proyecto de producci√≥n.
La IA debe actuar como mentor, explicando y ense√±ando los conceptos, revisando el c√≥digo que yo escriba y corrigi√©ndome si es necesario, pero no debe escribir c√≥digo por m√≠ directamente. Yo escribir√© cada l√≠nea, y la IA solo me guiar√°.

Ì¥π 1. Configuraci√≥n inicial del proyecto

Tecnolog√≠as: Python 3.10+, FastAPI, Uvicorn.
Objetivos:

Crear un entorno virtual.

Instalar dependencias necesarias.

Configurar el punto de entrada main.py con un endpoint de prueba (/health).

Ì±â Mentor: debe explicar la estructura de un proyecto FastAPI y por qu√© usamos uvicorn como servidor ASGI.

Ì¥π 2. Modelo de datos y CRUD b√°sico

Tecnolog√≠as: FastAPI, Pydantic.
Objetivos:

Definir un modelo Task con campos: id, description, due_date, priority, status.

Implementar endpoints REST:

POST /tasks (crear tarea).

GET /tasks (listar todas las tareas).

PUT /tasks/{id} (actualizar una tarea).

DELETE /tasks/{id} (eliminar tarea).

Ì±â Mentor: debe ense√±ar la diferencia entre modelos de entrada (request) y salida (response) en Pydantic, y explicar c√≥mo FastAPI valida autom√°ticamente los datos.

Ì¥π 3. Persistencia de datos

Tecnolog√≠as: SQLite + SQLAlchemy (opcional, se puede usar una lista en memoria primero).
Objetivos:

Empezar con almacenamiento en memoria (diccionario o lista).

Luego, opcionalmente, conectar una base SQLite usando SQLAlchemy.

Ì±â Mentor: explicar qu√© es una base de datos relacional y por qu√© usar SQLite como paso intermedio para un MVP.

Ì¥π 4. Endpoint de NLP para crear tareas desde lenguaje natural

Tecnolog√≠as: spaCy (o regex + heur√≠sticas si queremos algo m√°s simple).
Objetivos:

Crear un endpoint POST /tasks/nlp que reciba frases como:

‚ÄúRecu√©rdame enviar el reporte el lunes a las 9 am con prioridad alta‚Äù.

Parsear la frase y devolver una tarea estructurada:
