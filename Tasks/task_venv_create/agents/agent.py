import sys
import os
import subprocess
import logging

def run_command(command):
   result= subprocess.run(command, shell=True, capture_output=True)
   return result.stdout.strip(),result.stderr.strip()

def create_venv(venv_name):
    task_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    project_root = os.path.dirname(os.path.dirname(task_dir))

    run_command(f"cd {task_dir} && python3 -m venv {venv_name}")

    run_command(f"cd {task_dir} && source {venv_name}/bin/activate")

    run_command(f"cd {task_dir} && pip install -r {project_root}/requirements.txt")

def deactivate_venv():
    task_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    run_command(f"cd {task_dir} && deactivate")

if __name__ == "__main__":
    create_venv("venv")