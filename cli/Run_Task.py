import click  # type: ignore
import sys
from pathlib import Path
import uuid
sys.path.insert(0, str(Path(__file__).parent.parent / "Tasks"))
import uuid


@click.command("run_task")
@click.option('--task_name', prompt='Task Name', help='Name of the task to run.')


def run_task(task_name, **kwargs):
    run_id=str(uuid.uuid4())
    kwargs['run_id']=run_id
    task_module = __import__(f'{task_name}.main', fromlist=['main'])
    task_module.main(task_name, **kwargs)
    click.echo(f'RUN ID: {run_id}')
    return run_id
if __name__ == '__main__':
    run_task()