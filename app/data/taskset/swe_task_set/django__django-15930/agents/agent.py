import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('63884829acd207404f2a5c3cc1d6b4cd0a822b70')
        print(f"Checked out 63884829acd207404f2a5c3cc1d6b4cd0a822b70")
    except Exception as e:
        print(f"Failed to check out 63884829acd207404f2a5c3cc1d6b4cd0a822b70: {e}")

if __name__ == "__main__":
    main()
