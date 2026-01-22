import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('f83b44075dafa429d59e8755aa47e15577cc49f9')
        print(f"Checked out f83b44075dafa429d59e8755aa47e15577cc49f9")
    except Exception as e:
        print(f"Failed to check out f83b44075dafa429d59e8755aa47e15577cc49f9: {e}")

if __name__ == "__main__":
    main()
