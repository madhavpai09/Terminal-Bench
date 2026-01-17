import argparse
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from client import client_user


def main():
    parser = argparse.ArgumentParser(description='Run a task')
    parser.add_argument('--task_name', help='Name of the task')
    parser.add_argument('--venv_name', help='Name of venv')
    
    args = parser.parse_args()
    
    task_name = args.task_name
    if not task_name:
        task_name = input('Task Name: ')
    
    kwargs = {}
    if task_name == 'task_venv_create':
        venv_name = args.venv_name
        if not venv_name:
            venv_name = input('venv_name: ')
        kwargs['venv_name'] = venv_name
    
    print(f"Running task '{task_name}'...")
    result = client_user.run_request(task_name, **kwargs)
    
    if 'error' in result:
        print(f" {result['error']}")
        sys.exit(1)

    output = result.get('output', {})
    print(f"Run ID: {output.get('run_id', 'N/A')}")
    print(f"Status: {output.get('status', 'N/A')}")
    
    if 'error' in output:
        print(f"Error details: {output['error']}")


if __name__ == '__main__':
    main()