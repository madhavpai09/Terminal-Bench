from fastapi import APIRouter
import sys
sys.path.append("../")
from cli.New_Task import invoke_task
from cli.setup import setup


router = APIRouter()

@router.post("/create")
def create_task():
    task_name = invoke_task()
    return {"task_name": task_name}

@router.post("/run")
def run_task():
    task_name = setup()
    return {"task_name": task_name}
