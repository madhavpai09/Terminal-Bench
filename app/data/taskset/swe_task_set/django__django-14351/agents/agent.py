import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('06fd4df41afb5aa1d681b853c3c08d8c688ca3a5')
        print(f"Checked out 06fd4df41afb5aa1d681b853c3c08d8c688ca3a5")
    except Exception as e:
        print(f"Failed to check out 06fd4df41afb5aa1d681b853c3c08d8c688ca3a5: {e}")

if __name__ == "__main__":
    main()
