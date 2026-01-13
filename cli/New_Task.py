from core.Task_creator import main
import click # type: ignore


@click.command("invoke")
@click.option('--task_name', prompt='New Task Name', help='Name of the new task to create.')


def invoke(task_name):
    main(task_name)

if __name__ == '__main__':
    invoke()