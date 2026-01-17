import subprocess
import os
import sys
import jinja2

base_dir=os.path.dir(os.path.dir(os.path.abspath(__file__)))
sys.path.append(base_dir)
from models import models
    
def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)

def main(task : models.TaskCreate):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    tasks_dir = os.path.join(base_dir, 'Tasks')
    task_dir = os.path.join(tasks_dir, task.task_name)
    
    os.makedirs(task_dir, exist_ok=True)
    create_task_structure(task, task_dir)

def create_task_structure(task: models.TaskCreate, task_dir: str):
    os.makedirs(os.path.join(task_dir, 'agents'), exist_ok=True)
    os.makedirs(os.path.join(task_dir, 'solutions'), exist_ok=True)
    os.makedirs(os.path.join(task_dir, 'tests'), exist_ok=True)
    os.makedirs(os.path.join(task_dir, 'results'), exist_ok=True)
    with open (os.path.join(task_dir, '__init__.py'), 'w'):
        pass
    with open (os.path.join(task_dir, 'main.py'), 'w'):
        pass
    with open (os.path.join(task_dir, 'tasks.yaml'), 'w'):
        pass

    template_dir = os.path.join(os.path.dirname(__file__),'templates')
    env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))
    template = env.get_template('main.jinja')
    output = template.render(task_name=task.task_name)
    with open(os.path.join(task_dir, 'main.py'), 'w') as f:
        f.write(output)

if __name__ == "__main__":
   main(task=models.TaskCreate(task_name="SampleTask"))