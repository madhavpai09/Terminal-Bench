import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('e6588aa4e793b7f56f4cadbfa155b581e0efc59a')
        print(f"Checked out e6588aa4e793b7f56f4cadbfa155b581e0efc59a")
    except Exception as e:
        print(f"Failed to check out e6588aa4e793b7f56f4cadbfa155b581e0efc59a: {e}")

if __name__ == "__main__":
    main()
