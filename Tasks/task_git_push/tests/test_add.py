import subprocess
import os

def test_git_add():
    # Verify that the task directory has no unstaged changes.
    # We focus on the task directory specifically.
    task_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    result = subprocess.run(f"git status {task_dir}", shell=True, capture_output=True, text=True)
    assert "Changes not staged for commit" not in result.stdout

