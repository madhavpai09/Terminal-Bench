import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/pytest-dev/pytest"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('3c1534944cbd34e8a41bc9e76818018fadefc9a1')
        print(f"Checked out 3c1534944cbd34e8a41bc9e76818018fadefc9a1")
    except Exception as e:
        print(f"Failed to check out 3c1534944cbd34e8a41bc9e76818018fadefc9a1: {e}")

if __name__ == "__main__":
    main()
