import subprocess
import os
def run_command(command):
    result = subprocess.run(command,shell=True,capture_output=True)
    return result.stdout.strip(),result.stderr.strip()


def dependency_check():
    command = "pip -m check"
    result = run_command(command)
    assert "No broken requirements found." in result


if __name__ =='__main__':
    dependency_check()

