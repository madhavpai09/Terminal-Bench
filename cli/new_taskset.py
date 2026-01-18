import click
import sys
import os

# Ensure project root is in path
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if base_dir not in sys.path:
    sys.path.append(base_dir)

from client import client_user

@click.command("create_taskset")
@click.option("--taskset_name",prompt="Task Set Name")

def create_taskset():
    click.secho("Enter your Task Set Name : ")
    name = input()
    taskset_create_request(name)

if __name__ == '__main__':
    create_taskset()