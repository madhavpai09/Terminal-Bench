import sys
import os
from fastapi import APIRouter
base_dir=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(base_dir)
from models import models
from app.core import Task_creator, Task_runner 
from app.core.task import Task

router = APIRouter(prefix="/tasks")


@router.post("/create/{task_name}")
def create_task(task_name: str):
    task_create = models.TaskCreate(task_name=task_name)
    task = Task(task_create)
    task.create()
    return {"message": "Task created successfully"}

@router.post("/run/{task_name}")

def run_task(task_name: str):
    try:
        output =  Task_runner.run_task(task_name)

        return {"message": "Task run finished", "output": output}
    except Exception as e:
        return {"message": "Task run failed", "error": str(e)}, 500
