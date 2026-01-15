import subprocess
from time import sleep
from pathlib import Path
import os

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)
    return result.stdout.strip(), result.stderr.strip()

def main():
    base_dir= os.path.dirname(os.path.abspath(__file__))
    command = 'cd {base_dir}/results && touch hello.py && echo "print(\'Hellly, world!\')" > hello.py'
    run_command(command)
    command = 'cd {base_dir}/results && touch result.txt && python hello.py > result.txt'
    run_command(command)

if __name__ == "__main__":
    main()