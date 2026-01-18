import sys
import os
from fastapi import APIRouter

base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if base_dir not in sys.path:
    sys.path.append(base_dir)

from models import model
from app.core import task

router = APIRouter(prefix="/tasks")


@router.post("/create")
def create_task(task_create: model.TaskCreate):
    try:
        task.Task.create(task_create)
        return {"message": "Task created successfully", "name": task_create.name}
    except Exception as e:
        return {"message": "Task creation failed", "error": str(e)}

@router.post("/run/{task_name}")
def run_task(task_name: str):
    try:
        task_obj = task.Task.get(task_name)
        output = task_obj.run()
        return {"message": "Task run finished", "output": output}
    except Exception as e:
        return {"message": "Task run failed", "error": str(e)}

