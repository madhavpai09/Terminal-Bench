import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)
    return result.stdout.strip(), result.stderr.strip() 

def main(): 
    print("Task Name:")
    task_name = input().strip()

    command = f'cd /Users/jmadhavpai/Desktop/Terminal-bench/Tasks/{task_name}/results && touch hello.py && echo "print(\'Hellly, world!\')" > hello.py'
    run_command(command)

    command = f'cd /Users/jmadhavpai/Desktop/Terminal-bench/Tasks/{task_name}/results && touch result.txt && python hello.py > result.txt'
    run_command(command)

    print("Task execution completed.")
    status = "verification_pending"
    command = f'cd /Users/jmadhavpai/Desktop/Terminal-bench/Tasks/{task_name}/tests && python task_verify.py'
    run_command(command)
    status = "verification_complete"

    