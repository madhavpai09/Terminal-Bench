import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('652c68ffeebd510a6f59e1b56b3e007d07683ad8')
        print(f"Checked out 652c68ffeebd510a6f59e1b56b3e007d07683ad8")
    except Exception as e:
        print(f"Failed to check out 652c68ffeebd510a6f59e1b56b3e007d07683ad8: {e}")

if __name__ == "__main__":
    main()
