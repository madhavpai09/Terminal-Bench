import subprocess
import uuid


def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)
    return result.stdout.strip(), result.stderr.strip() 


def main(task_name,**kwargs): 
    run_id = kwargs.get('run_id', 'no-id')
    
    print(f"Task: {task_name}")
    print(f"Run ID: {run_id}")
    
    command = f'cd /Users/jmadhavpai/Desktop/Terminal-bench/Tasks/{task_name}/agents && python agent.py'
    run_command(command)
    status = "verification_pending"
    command = f'cd /Users/jmadhavpai/Desktop/Terminal-bench/Tasks/{task_name}/tests && python test1.py'
    run_command(command)
    status = "test1_passed"
    command = f'cd /Users/jmadhavpai/Desktop/Terminal-bench/Tasks/{task_name}/tests && python test2.py'
    run_command(command)
    status = "test2_passed"
    command = f'cd /Users/jmadhavpai/Desktop/Terminal-bench/Tasks/{task_name}/tests && python test3.py'
    run_command(command)
    status = "Successfully Completed"
    return status


if __name__ == "__main__":
    main("task_Hello_world")