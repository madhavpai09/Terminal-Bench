import click
import sys
import os
from client import client_user

@click.command("create_taskset")
@click.option("--taskset_name",prompt="Task Set Name")

def create_taskset():
    click.secho("Enter your Task Set Name : ")
    name = input()
    taskset_create_request(name)

if __name__ == '__main__':
    create_taskset()