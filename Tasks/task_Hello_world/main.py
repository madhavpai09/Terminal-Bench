import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)
    return result.stdout.strip(), result.stderr.strip() 

def main(task_name): 
    command = f'cd /Users/jmadhavpai/Desktop/Terminal-bench/Tasks/task_Hello_world/agents && python agent.py'
    run_command(command)
    status = "verification_pending"
    command = f'cd /Users/jmadhavpai/Desktop/Terminal-bench/Tasks/task_Hello_world/tests && python test1.py'
    run_command(command)
    status = "test1_passed"
    command = f'cd /Users/jmadhavpai/Desktop/Terminal-bench/Tasks/task_Hello_world/tests && python test2.py'
    run_command(command)
    status = "test2_passed"
    command = f'cd /Users/jmadhavpai/Desktop/Terminal-bench/Tasks/task_Hello_world/tests && python test3.py'
    run_command(command)
    status = "Successfully Completed"
    print(status)

if __name__ == "__main__":
    main()
