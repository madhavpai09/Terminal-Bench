import os
import sys
import pytest
import logging
from typing import Optional

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)
sys.path.append(os.path.join(current_dir, 'agents'))
from agents import agent

def main(task_name, **kwargs):
    logger = init_logger(task_name)
    agent.main()

    test_dir = os.path.join(current_dir, 'tests')

    retcode = pytest.main([
        "-v",
        os.path.join(test_dir, 'test_add.py'),
        os.path.join(test_dir, 'test_commit.py'),
        os.path.join(test_dir, 'test_push.py')
    ])
    
    if retcode == 0:
        logger.info("All verification tests passed!")
    else:
        logger.info(f"Tests failedte")


def init_logger(task_name: str, log_level: int = logging.INFO):
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
    main("task_git_push")