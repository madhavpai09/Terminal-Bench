import os
import sys
base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(base_dir)
from models.model import TaskCreate
from pydantic import BaseModel
from typing import Optional

class Task(BaseModel):
    task_name: str
    description : Optional[str] = None

    def __init__(self, task_create: TaskCreate):
        self.task_name = task_create.name
        self.description = task_create.description

    def run(self):
        run_id = str(uuid.uuid4())
        kwargs['run_id'] = run_id
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

    def create(task : TaskCreate):
        app_dir =os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        tasks_dir = os.path.join(app_dir,'data','Tasks')
        task_dir = os.path.join(tasks_dir, task.task_name)
    
        os.makedirs(task_dir, exist_ok=True)
        Task._create_task_structure(task, task_dir)

    @staticmethod
    def _create_task_structure(task: TaskCreate, task_dir: str):
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
