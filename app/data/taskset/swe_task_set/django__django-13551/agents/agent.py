import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('7f9e4524d6b23424cf44fbe1bf1f4e70f6bb066e')
        print(f"Checked out 7f9e4524d6b23424cf44fbe1bf1f4e70f6bb066e")
    except Exception as e:
        print(f"Failed to check out 7f9e4524d6b23424cf44fbe1bf1f4e70f6bb066e: {e}")

if __name__ == "__main__":
    main()
