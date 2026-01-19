import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from client import client_user

from models import model

import click # type: ignore


@click.command("invoke_task")
@click.option('--task_name', prompt='New Task Name', help='Name of the new task to create.')
@click.option('--taskset_name', prompt='Taskset Name', help='Name of the taskset to which the task belongs.')
@click.option('--description', default="", help='Description of the new task.')
@click.option('--instruction', prompt='Instruction', help='Instruction for the new task.')
@click.option('--complexity', default="", help='Complexity of the new task.')
@click.option('--priority', default="", help='Priority of the new task.')
@click.option('--environment', default="", help='Environment of the new task.')


def invoke_task(task_name:str, taskset_name:str, description:str, instruction:str, complexity:str, priority:str, environment:str)->str:
    request = model.TaskCreate(
        name=task_name,
        taskset_name=taskset_name,
        description=description,
        instruction=instruction,
        complexity=complexity,
        priority=priority,
        environment=environment
    )
    client_user.task_create_request(request.dict())

    return task_name


if __name__ == '__main__':
    invoke_task()