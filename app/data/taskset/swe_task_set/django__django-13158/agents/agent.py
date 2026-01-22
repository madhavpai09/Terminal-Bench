import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('7af8f4127397279d19ef7c7899e93018274e2f9b')
        print(f"Checked out 7af8f4127397279d19ef7c7899e93018274e2f9b")
    except Exception as e:
        print(f"Failed to check out 7af8f4127397279d19ef7c7899e93018274e2f9b: {e}")

if __name__ == "__main__":
    main()
