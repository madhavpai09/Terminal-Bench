import click
import os
import sys
import pexpect 


sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def run_task_logic(task_name):
    project_root = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
    cmd = f"docker run --rm -it -v {project_root}:/app terminal_bench"
    try:
        child = pexpect.spawn(cmd, encoding='utf-8', timeout=30)

        index = child.expect(['Task Name: ', pexpect.EOF, pexpect.TIMEOUT])
        
        if index == 0:
            child.sendline(task_name)
            child.expect(pexpect.EOF) 
            return child.before
        elif index == 1:
            output = child.before
            raise Exception(f"Docker process terminated unexpectedly. Output: {output}")
        else:
            raise Exception("Timed out waiting for 'Task Name: ' prompt from Docker container.")
            
    except pexpect.exceptions.ExceptionPexpect as e:
        raise Exception(f"Failed to start/communicate with Docker: {str(e)}")

@click.command("setup_run")
def setup_run():

    tasks_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'Tasks')
    tasks = [d for d in os.listdir(tasks_dir) if os.path.isdir(os.path.join(tasks_dir, d))]
    click.echo("Available tasks:")
    for task in tasks:
        click.echo(f"- {task}")

    task_name = click.prompt("Enter the task name to run", type=str)
    result = run_task_logic(task_name)
    click.echo(result)
    return task_name


if __name__ == '__main__':
    setup_run(standalone_mode=False)