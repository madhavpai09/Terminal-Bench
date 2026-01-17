import subprocess
import os

def run_command(command):
    result = subprocess.run(command,shell=True,capture_output=True)
    return result.stdout.strip(),result.stderr.strip()


def test_activation(venv_name):
    root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    res = run_command("which python")
    assert f"{venv_name}/bin/python" in res[0]

if "__main__"==__name__:
    test_activation()