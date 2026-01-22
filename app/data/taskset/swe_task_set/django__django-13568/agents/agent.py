import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('ede9fac75807fe5810df66280a60e7068cc97e4a')
        print(f"Checked out ede9fac75807fe5810df66280a60e7068cc97e4a")
    except Exception as e:
        print(f"Failed to check out ede9fac75807fe5810df66280a60e7068cc97e4a: {e}")

if __name__ == "__main__":
    main()
