import click # type: ignore
import importlib

@click.command("run_task")
@click.option('--task_name', prompt='Task Name', help='Name of the task to run.')
def run_task(task_name):
    module_path = f'{task_name}.main'
    module = importlib.import_module(module_path)
    module.main(task_name)

if __name__ == '__main__':
    run_task()