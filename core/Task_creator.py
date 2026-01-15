import subprocess
import os

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)

def main(task_name):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    tasks_dir = os.path.join(base_dir, 'Tasks')
    
    command = f'cd {tasks_dir} && mkdir {task_name} && cd {task_name} && mkdir agents results tests solutions && touch main.py tasks.yaml'
    run_command(command)
    command = f'cd {tasks_dir}/{task_name}/agents && touch agent.py'
    run_command(command)


if __name__ == "__main__":
    main(task_name)    