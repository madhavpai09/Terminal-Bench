import subprocess
import os
from typing import Optional
from pydantic import BaseModel

class TaskCreate(BaseModel):
    task_name: str
    description : Optional[str] = None
    agents:bool = True
    solutions:bool = True
    tests:bool = True
    main_py:bool = True
    tasks_yaml:bool = True
    results:bool = True

    
def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)

def main(task : TaskCreate):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    tasks_dir = os.path.join(base_dir, 'Tasks')
    task_dir = os.path.join(tasks_dir, task.task_name)
    
    os.makedirs(task_dir, exist_ok=True)

    if task.agents:
        os.makedirs(os.path.join(task_dir, 'agents'), exist_ok=True)
    if task.solutions:
        os.makedirs(os.path.join(task_dir, 'solutions'), exist_ok=True)
    if task.tests:
        os.makedirs(os.path.join(task_dir, 'tests'), exist_ok=True)
    if task.results:
        os.makedirs(os.path.join(task_dir, 'results'), exist_ok=True)
    if task.main_py:
        with open (os.path.join(task_dir, 'main.py'), 'w'):
            pass
    if task.tasks_yaml:
        with open (os.path.join(task_dir, 'tasks.yaml'), 'w'):
            pass


if __name__ == "__main__":
   main(task=TaskCreate(task_name="SampleTask"))