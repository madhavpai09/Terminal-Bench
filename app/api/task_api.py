import sys
import os
from fastapi import APIRouter

# Ensure project root is in path
base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if base_dir not in sys.path:
    sys.path.append(base_dir)

from models import model
from app.core import task

router = APIRouter(prefix="/tasks")


@router.post("/run/{task_name}")
def run_task(task_name: str):
    try:
        output =  task.run(task_name)

        return {"message": "Task run finished", "output": output}
    except Exception as e:
        return {"message": "Task run failed", "error": str(e)}

