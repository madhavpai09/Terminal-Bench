import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('ce69e34bd646558bb44ea92cecfd98b345a0b3e0')
        print(f"Checked out ce69e34bd646558bb44ea92cecfd98b345a0b3e0")
    except Exception as e:
        print(f"Failed to check out ce69e34bd646558bb44ea92cecfd98b345a0b3e0: {e}")

if __name__ == "__main__":
    main()
