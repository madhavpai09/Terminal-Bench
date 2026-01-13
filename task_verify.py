import os
import subprocess

directory = "/Users/jmadhavpai/Desktop/Terminal-bench/Tasks"
for file in os.listdir(directory):
    if file.endswith(".py"):
        file_path = os.path.join(directory, file)
        subprocess.run(["python", file_path])
        print(f"Executed {file_path}")
        