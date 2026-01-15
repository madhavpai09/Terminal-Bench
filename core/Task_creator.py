import subprocess
import os
from typing import Optional
from pydantic import BaseModel


class TaskCreate(BaseModel):
    task_name: str
    description : Optional[str] = None

    
def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)

def main(task : TaskCreate):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    tasks_dir = os.path.join(base_dir, 'Tasks')
    task_dir = os.path.join(tasks_dir, task.task_name)
    
    os.makedirs(task_dir, exist_ok=True)
    create_task_structure(task, task_dir)

def create_task_structure(task: TaskCreate, task_dir: str):
    os.makedirs(os.path.join(task_dir, 'agents'), exist_ok=True)
    os.makedirs(os.path.join(task_dir, 'solutions'), exist_ok=True)
    os.makedirs(os.path.join(task_dir, 'tests'), exist_ok=True)
    os.makedirs(os.path.join(task_dir, 'results'), exist_ok=True)
    with open (os.path.join(task_dir, 'main.py'), 'w'):
        pass
    with open (os.path.join(task_dir, 'tasks.yaml'), 'w'):
        pass


if __name__ == "__main__":
   main(task=TaskCreate(task_name="SampleTask"))