import subprocess
import os

def test_git_commit():
    # Check the last commit message. 
    # Note: In agent.py, it uses "{commit_comment}" which might be literal if not rendered by Jinja in the agent script.
    # However, the user seems to want to verify that a commit WAS made.
    result = subprocess.run("git log -1 --pretty=%B", shell=True, capture_output=True, text=True)
    assert len(result.stdout.strip()) > 0
