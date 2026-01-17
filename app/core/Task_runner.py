import os
import sys
import uuid
from pathlib import Path
from typing import Dict, Any

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
tasks_dir = os.path.join(base_dir, 'data', 'Tasks')
sys.path.insert(0, tasks_dir)


def run_task(task_name: str, **kwargs):
    run_id = str(uuid.uuid4())
    kwargs['run_id'] = run_id
        
    task_module = __import__(f'{task_name}.main', fromlist=['main'])

    status = task_module.main(task_name, **kwargs)
        
    if not status:
        status = kwargs.get('status', 'completed')
        
    return {
        "run_id": run_id,
        "status": status,
        "task_name": task_name
    }
        
