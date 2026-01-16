import os
import sys
import pytest
import logging
from typing import Optional

# Add the current directory and agents directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)
sys.path.append(os.path.join(current_dir, 'agents'))

try:
    from agents import agent
except ImportError:
    # Fallback if structure is slightly different
    import agent

def main(task_name, **kwargs):
    print(f"--- Starting Task: {task_name} ---")
    
    # Initialize logger
    init_logger(task_name)
    
    # 1. Run the Agent
    print("\n[1/2] Running agent...")
    agent.main()
    
    # 2. Run verification tests
    print("\n[2/2] Running verification tests...")
    test_dir = os.path.join(current_dir, 'tests')
    
    # Run pytests and capture results
    retcode = pytest.main([
        "-v",
        os.path.join(test_dir, 'test_add.py'),
        os.path.join(test_dir, 'test_commit.py'),
        os.path.join(test_dir, 'test_push.py')
    ])
    
    if retcode == 0:
        print("\nSUCCESS: All verification tests passed!")
    else:
        print(f"\nFAILURE: Tests failed with exit code {retcode}")


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