import os
import subprocess

def test_venv_created(venv_name):
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    venv_path = os.path.join(project_root, "{venv_name}")
    assert os.path.isdir(venv_path), print("failed to creat venv")

