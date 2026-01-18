import os
import sys
from pathlib import Path
from fastapi import APIRouter
from app.core.taskset import TaskSet
from app.core.task import Task
from models import model


router = APIRouter(prefix="/tasksets")

@router.post("/create/{taskset_name}")
def create_taskset(taskset_name: str):
    taskset_create = model.TaskSetCreate(name=taskset_name)
    taskset = TaskSet.create(taskset_create)
    return taskset


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
