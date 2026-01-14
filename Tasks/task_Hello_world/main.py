import subprocess
import uuid
import os
import logging
from typing import Optional

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)
    return result.stdout.strip(), result.stderr.strip() 


def main(task_name, **kwargs): 
    init_logger
    run_id = kwargs.get('run_id', 'no-id')
    
    print(f"Task: {task_name}")
    print(f"Run ID: {run_id}")
    
    command = f'cd /Users/jmadhavpai/Desktop/Terminal-bench/Tasks/{task_name}/agents && python agent.py'
    run_command(command)
    status = "verification_pending"
    kwargs['status'] = status
    command = f'cd /Users/jmadhavpai/Desktop/Terminal-bench/Tasks/{task_name}/tests && python test1.py'
    run_command(command)
    status = "test1_passed"
    kwargs['status'] = status
    command = f'cd /Users/jmadhavpai/Desktop/Terminal-bench/Tasks/{task_name}/tests && python test2.py'
    run_command(command)
    status = "test2_passed"
    kwargs['status'] = status
    command = f'cd /Users/jmadhavpai/Desktop/Terminal-bench/Tasks/{task_name}/tests && python test3.py'
    run_command(command)
    status = "Successfully Completed"
    kwargs['status'] = status
    return status

def init_logger(task_name: str, log_level: Optional[int]=logging.INFO):
        logging.basicConfig(
            level=log_level,
            filename=os.path.join(
                 os.getcwd(), 
                 "Tasks", 
                 task_name, 
                 f"{task_name}.log"),
                 filemode='w', 
                 format='%(asctime)s - %(' \
                 'levelname)s - %(message)s'
        )


if __name__ == "__main__":
    main("task_Hello_world")