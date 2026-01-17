import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from client.client_user import create_request 

from models import models

import click # type: ignore


@click.command("invoke_task")
@click.option('--task_name', prompt='New Task Name', help='Name of the new task to create.')


def invoke_task(task_name:models.TaskCreate)->models.TaskCreate:
    request = models.TaskCreate(task_name=task_name)
    create_request(task_name)
    return task_name


if __name__ == '__main__':
    invoke_task()