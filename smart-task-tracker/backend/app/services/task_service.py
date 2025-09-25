from fastapi import HTTPException
from app.models import Task

tasks_db = []

def create_task(task: Task):
    tasks_db.append(task.dict())
    return {"status": "Task created", "task": task}

def get_all_tasks():
    return tasks_db

def get_task(task_id: int):
    for task in tasks_db:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

def update_task(task_id: int, updated: Task):
    for index, task in enumerate(tasks_db):
        if task["id"] == task_id:
            tasks_db[index] = updated.dict()
            return {"status": "Task updated", "task": updated}
    raise HTTPException(status_code=404, detail="Task not found")

def delete_task(task_id: int):
    for index, task in enumerate(tasks_db):
        if task["id"] == task_id:
            deleted = tasks_db.pop(index)
            return {"status": "Task deleted", "task": deleted}
    raise HTTPException(status_code=404, detail="Task not found")