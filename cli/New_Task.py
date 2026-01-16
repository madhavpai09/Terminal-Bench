import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from client.client_user import main as client_main

from core import Task_creator
from core.Task_creator import TaskCreate, main
import click # type: ignore


@click.command("invoke_task")
@click.option('--task_name', prompt='New Task Name', help='Name of the new task to create.')


def invoke_task(task_name:Task_creator):
    request = TaskCreate(task_name=task_name)
    main(task=request)
    client_main(task_name)
    return task_name


if __name__ == '__main__':
    invoke_task()