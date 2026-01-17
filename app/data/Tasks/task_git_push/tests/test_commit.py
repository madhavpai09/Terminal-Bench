import subprocess
import os

def test_git_commit():

    result = subprocess.run("git log -1 --pretty=%B", shell=True, capture_output=True, text=True)
 
    assert len(result.stdout.strip()) > 0
