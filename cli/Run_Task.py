import argparse
import sys
from pathlib import Path
import uuid
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from client.client_user import main as client_main
sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent.parent / "Tasks"))


def return_status(task_name, **kwargs):
    run_id = str(uuid.uuid4())
    kwargs['run_id'] = run_id
    task_module = __import__(f'{task_name}.main', fromlist=['main'])
    status = task_module.main(task_name, **kwargs)
    if not status:
        status = kwargs.get('status', 'unknown')
    return {"run_id": run_id, "status": status}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run a task')
    parser.add_argument('--task_name', help='Name of the task to run.')
    parser.add_argument('--venv_name', help='Name of the virtual environment (for task_venv_create).')
    args = parser.parse_args()

    task_name = args.task_name
    if not task_name:
        task_name = input('Task Name: ')

    kwargs = {}
    if task_name == 'task_venv_create':
        venv_name = args.venv_name
        if not venv_name:
            venv_name = input('venv_name: ')
        kwargs['venv_name'] = venv_name

    res = return_status(task_name, **kwargs)
    client_main(task_name)
    print(f"Run ID: {res['run_id']}")
    print(f"Status: {res['status']}")