import os
import sys
from pathlib import Path
base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if base_dir not in sys.path:
    sys.path.append(base_dir)
from fastapi import APIRouter
from models.model import TaskSetCreate
from app.core.taskset import TaskSet
from app.core.task import Task


router = APIRouter(prefix="/tasksets")

@router.post("/create/{taskset_name}")
def create_taskset(taskset_name: str):
    taskset_create = TaskSetCreate(name=taskset_name, tasks=[])
    taskset = TaskSet.create(taskset_create)
    return {"message": "Taskset created", "name": taskset.task_set_name}


@router.post("/add/{taskset_name}/{task_name}")
def add_task(taskset_name: str, task_name: str):
    taskset = TaskSet.get(taskset_name)
    task = Task.get(task_name)
    taskset.add_task(task)
    return taskset  


@router.post("/run/{taskset_name}")
def run_taskset(taskset_name: str):
    taskset = TaskSet.get(taskset_name)
    taskset.run()
    return taskset
