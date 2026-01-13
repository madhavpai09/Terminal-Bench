import click  # try: ignore
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "Tasks"))

@click.command("run_task")
@click.option('--task_name', prompt='Task Name', help='Name of the task to run.')
def run_task(task_name, **kwargs):
    task_module = __import__(f'{task_name}.main', fromlist=['main'])
    task_module.main(task_name, **kwargs)

if __name__ == '__main__':
    run_task()