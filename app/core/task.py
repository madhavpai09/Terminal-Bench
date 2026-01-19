import os
import sys
from models.model import TaskCreate
from pydantic import BaseModel
from typing import Optional
import uuid
import jinja2

class Task:
    def __init__(self, name: str,instruction: str,description: Optional[str] = None, complexity: Optional[str] = None, priority: Optional[str] = None, environment: Optional[str] = None):
        self.task_name = name
        self.instruction = instruction
        self.description = description
        self.complexity = complexity
        self.priority = priority
        self.environment = environment

    def run(self):
        run_id = str(uuid.uuid4())
        kwargs = {'run_id' : run_id}
        task_name = self.task_name
        
        task_module = __import__(f'{task_name}.main', fromlist=['main'])

        status = task_module.main(task_name, **kwargs)
        
        if not status:
            status = kwargs.get('status', 'completed')
        
        return {
            "run_id": run_id,
            "status": status,
            "task_name": task_name
        }

    @staticmethod
    def get(name: str):
        return Task(name=name)

    @staticmethod
    def create(task : TaskCreate):
        app_dir =os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        tasks_dir = os.path.join(app_dir, 'data', 'taskset', task.taskset_name)
        task_dir = os.path.join(tasks_dir, task.name)
    
        os.makedirs(task_dir, exist_ok=True)
        Task._create_task_structure(task, task_dir, task.taskset_name)


    @staticmethod
    def _create_task_structure(task: TaskCreate, task_dir: str, taskset_name: str):
        os.makedirs(os.path.join(task_dir, 'agents'), exist_ok=True)
        os.makedirs(os.path.join(task_dir, 'solutions'), exist_ok=True)
        os.makedirs(os.path.join(task_dir, 'tests'), exist_ok=True)
        os.makedirs(os.path.join(task_dir, 'results'), exist_ok=True)
        with open (os.path.join(task_dir, '__init__.py'), 'w'):
            pass
        with open (os.path.join(task_dir, 'main.py'), 'w'):
            pass
        with open (os.path.join(task_dir, 'tasks.yaml'), 'w') as f:
            f.write(f"instructions:  \\n/t {task.instruction}\\n")
            f.write(f"description:  \\n/t {task.description}\\n")
            f.write(f"complexity:  \\n/t {task.complexity}\\n")
            f.write(f"priority:  \\n/t {task.priority}\\n")
            f.write(f"environment:  \\n/t {task.environment}\\n") 

        template_dir = os.path.join(os.path.dirname(__file__),'templates')
        env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))
        template = env.get_template('main.jinja')
        output = template.render(task_name=task.name)
        with open(os.path.join(task_dir, 'main.py'), 'w') as f:
            f.write(output)
