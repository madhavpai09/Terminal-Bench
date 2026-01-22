import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/pylint-dev/pylint"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('684a1d6aa0a6791e20078bc524f97c8906332390')
        print(f"Checked out 684a1d6aa0a6791e20078bc524f97c8906332390")
    except Exception as e:
        print(f"Failed to check out 684a1d6aa0a6791e20078bc524f97c8906332390: {e}")

if __name__ == "__main__":
    main()
