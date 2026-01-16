import click  # type: ignore
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


@click.command("run_task")
@click.option('--task_name', prompt='Task Name', help='Name of the task to run.')


def run_task(task_name, **kwargs):
    res = return_status(task_name, **kwargs)
    client_main(task_name)
    click.echo(f"Run ID: {res['run_id']}")
    click.echo(f"Status: {res['status']}")


if __name__ == '__main__':
    run_task()