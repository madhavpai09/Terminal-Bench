import os
import sys
import subprocess
import jinja2

def run_command(command):
    result = subprocess.run(command,shell=True,capture_output=True,text=True)
    return result.stdout.strip(), result.stderr.strip()

def main():
    base_dir = sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

    command = f'cd {base_dir} && git add .'
    run_command(command)

    command = f'git commit -m "{{commit_comment}}"'
    run_command(command)

    command = f'git push origin main'
    run_command(command)
    
    
if __name__ == "__main__":
    main()