import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('98f6ada0e2058d67d91fb6c16482411ec2ca0967')
        print(f"Checked out 98f6ada0e2058d67d91fb6c16482411ec2ca0967")
    except Exception as e:
        print(f"Failed to check out 98f6ada0e2058d67d91fb6c16482411ec2ca0967: {e}")

if __name__ == "__main__":
    main()
