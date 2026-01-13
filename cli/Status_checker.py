import click
from Run_Task import run_task

@click.command("check_status")
@click.option('--task_name', prompt='Task Name', help='Name of the task to check status.')
def check_status(task_name):
    result = run_task.callback(task_name)
    
    click.echo(f"Run ID: {result['run_id']}")
    click.echo(f"Status: {result['status']}")
if __name__ == '__main__':
    check_status()