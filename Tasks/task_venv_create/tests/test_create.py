import os
import subprocess

def test_venv_created():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    venv_path = os.path.join(project_root, "venv")
    assert os.path.isdir(venv_path), print("ve")

