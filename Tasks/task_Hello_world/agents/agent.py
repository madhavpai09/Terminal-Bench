import subprocess
from time import sleep

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)
    return result.stdout.strip(), result.stderr.strip()

def main():
    
    command = 'cd /Users/jmadhavpai/Desktop/Terminal-bench/Tasks/task_Hello_world/results && touch hello.py && echo "print(\'Hello, world!\')" > hello.py'
    run_command(command)
    command = 'cd /Users/jmadhavpai/Desktop/Terminal-bench/Tasks/task_Hello_world/results && touch result.txt && python hello.py > result.txt'
    run_command(command)

if __name__ == "__main__":
    main()