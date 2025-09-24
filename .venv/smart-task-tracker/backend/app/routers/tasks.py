from fastapi import APIRouter, Depends, HTTPException
from app.models import Task
from app.services import task_service

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.post("/")
def create_task(task: Task):
    return task_service.create_task(task)

@router.get("/")
def get_tasks():
    return task_service.get_all_tasks()

@router.get("/{task_id}")
def get_task(task_id: int):
    return task_service.get_task(task_id)

@router.put("/{task_id}")
def update_task(task_id: int, updated_task: Task):
    return task_service.update_task(task_id, update_task)

@router.delete("/{task_id}")
def delete_task(task_id: int):
    return task_service.delete_task(task_id)