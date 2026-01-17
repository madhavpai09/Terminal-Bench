import sys
import os
from fastapi import APIRouter
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models import models
from client import client_user

router = APIRouter(prefix="/tasks")


@router.post("/create/{task_name}")
def create_task(task_name: str):
    task_create = models.TaskCreate(task_name=task_name)
    client_user.create_request(task=task_create)
    return {"message": "Task created successfully"}

@router.post("/run/{task_name}")

def run_task(task_name: str):
    try:
        output =  client_user.run_request(task_name)
        return {"message": "Task run finished", "output": output}
    except Exception as e:
        return {"message": "Task run failed", "error": str(e)}, 500
