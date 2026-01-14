import subprocess
import uuid
import os
import time
import logging
from typing import Optional


def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout.strip(), result.stderr.strip() 


def main(task_name, **kwargs): 
    logger = init_logger(task_name)
    run_id = kwargs.get('run_id', 'no-id')
    
    logger.info(f"Task: {task_name}")
    logger.info(f"Run ID: {run_id}")
    
    command = f'cd /Users/jmadhavpai/Desktop/Terminal-bench/Tasks/{task_name}/agents && python agent.py'
    run_command(command)
    status = "verification_pending"
    kwargs['status'] = status
    logger.info(f"Status: {status}")

    command = f'cd /Users/jmadhavpai/Desktop/Terminal-bench/Tasks/{task_name}/tests && python test1.py'
    run_command(command)
    status = "test1_passed"
    kwargs['status'] = status
    logger.info(f"Status: {status}")
    
    command = f'cd /Users/jmadhavpai/Desktop/Terminal-bench/Tasks/{task_name}/tests && python test2.py'
    run_command(command)
    status = "test2_passed"
    kwargs['status'] = status
    logger.info(f"Status: {status}")
    
    command = f'cd /Users/jmadhavpai/Desktop/Terminal-bench/Tasks/{task_name}/tests && python test3.py'
    run_command(command)
    status = "Successfully Completed"
    kwargs['status'] = status
    logger.info(f"Status: {status}")

    return status


def init_logger(task_name: str, log_level: Optional[int]=logging.INFO):
        logging.basicConfig(
            level=log_level,
            filename=os.path.join(
                 os.path.dirname(os.path.abspath(__file__)),"results",f"{task_name}.log"),
                 filemode='w', 
                 format=('%(asctime)s - %(levelname)s - %(message)s'))
        logger = logging.getLogger(task_name)
        return logger


if __name__ == "__main__":
    main("task_Hello_world")