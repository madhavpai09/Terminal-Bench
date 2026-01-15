from typing import Optional
from fastapi import FastAPI
import subprocess
import os
import logging


app = FastAPI()


@app.get("/")
async def root():       
    return {"message": "Hello World"}

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout.strip(), result.stderr.strip() 

@app.post("/run/{task_name}")
def main(task_name, **kwargs): 
    logger = init_logger(task_name)
    run_id = kwargs.get('run_id', 'no-id')
    
    logger.info(f"Task: {task_name}")
    logger.info(f"Run ID: {run_id}")
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    agents_dir = os.path.join(base_dir, 'agents')
    command = f'cd {agents_dir} && python agent.py'
    run_command(command)
    status = "verification_pending"
    kwargs['status'] = status
    logger.info(f"Status: {status}")
    return status

@app.post("/run/{task_name}/tests")
def run_tests(task_name, **kwargs):
    logger = init_logger(task_name)
    run_id = kwargs.get('run_id', 'no-id')
    
    logger.info(f"Task: {task_name}")
    logger.info(f"Run ID: {run_id}")
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(base_dir, 'tests')
    command = f'cd {tests_dir} && python test1.py'
    run_command(command)
    status = "test1_passed"
    kwargs['status'] = status
    logger.info(f"Status: {status}")
    
    command = f'cd {tests_dir} && python test2.py'
    run_command(command)
    status = "test2_passed"
    kwargs['status'] = status
    logger.info(f"Status: {status}")
    
    command = f'cd {tests_dir} && python test3.py'
    run_command(command)
    status = "Successfully Completed"
    kwargs['status'] = status
    logger.info(f"Status: {status}")

    return status


def init_logger(task_name: str, log_level: Optional[int]=logging.INFO):
        log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results")
        os.makedirs(log_dir, exist_ok=True)
        
        logging.basicConfig(
            level=log_level,
            filename=os.path.join(log_dir, f"{task_name}.log"),
            filemode='w', 
            format=('%(asctime)s - %(levelname)s - %(message)s'))
        logger = logging.getLogger(task_name)
        return logger


if __name__ == "__main__":
    main("task_Hello_world")