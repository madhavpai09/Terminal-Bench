import subprocess
import os

def test_git_push():

    result = subprocess.run("git status", shell=True, capture_output=True, text=True)
    assert "Your branch is up to date with 'origin/main'" in result.stdout
