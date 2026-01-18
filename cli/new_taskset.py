import click
import sys
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if base_dir not in sys.path:
    sys.path.append(base_dir)

from client import client_user

@click.command("create_taskset")
@click.option("--taskset_name",prompt="Task Set Name")

def create_taskset(taskset_name):
    click.secho(f"Creating Task Set: {taskset_name}")
    client_user.taskset_create_request(taskset_name)

if __name__ == '__main__':
    create_taskset()