from fastapi import FastAPI
from app.routers import tasks

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Smart Task Tracker")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Task API is running"}

app.include_router(tasks.router)


# app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
# app.include_router(users.router, prefix="/users", tags=["users"])

# @app.on_event("startup")
# async def startup():
#     init_db()

# @app.on_event("shutdown")
# async def shutdown():
#     close_db()





# from fastapi import FastAPI
# from pydantic import BaseModel

# class Task(BaseModel):
#     id: int
#     title: str
#     description: str
#     done: bool

# app = FastAPI()

# tasks = []

# @app.get("/")
# async def root():
#     return {"message": "Task API"}

# @app.post("/tasks/")
# async def create_task(task: Task):
#     tasks.append(task)
#     return {"status": "Task Created", "task": task}

# @app.get("/tasks/")
# async def get_tasks():
#     return{ "tasks": tasks}

# @app.get("/tasks/{id}")
# async def get_task_by_id(id: int):
#     for task in tasks:
#         if task.id == id:
#             return task

# @app.put("/tasks/{id}")
# async def update_task(id: int, updated_task: Task ):
#     for index, task in enumerate(tasks):
#         if task.id == id:
#             tasks[index] = updated_task
#             return {"status": "Task updated", "task": updated_task}
        
# @app.delete("/tasks/{id}")
# async def delete_task(id: int):
#     for index, task in enumerate(tasks):
#         if task.id == id:
#             deleted = tasks.pop(index)
#             return {"message": "Task deleted", "task": deleted}
