import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('5b884d45ac5b76234eca614d90c83b347294c332')
        print(f"Checked out 5b884d45ac5b76234eca614d90c83b347294c332")
    except Exception as e:
        print(f"Failed to check out 5b884d45ac5b76234eca614d90c83b347294c332: {e}")

if __name__ == "__main__":
    main()
