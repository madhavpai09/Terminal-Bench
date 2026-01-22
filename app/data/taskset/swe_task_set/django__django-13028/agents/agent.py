import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('78ad4b4b0201003792bfdbf1a7781cbc9ee03539')
        print(f"Checked out 78ad4b4b0201003792bfdbf1a7781cbc9ee03539")
    except Exception as e:
        print(f"Failed to check out 78ad4b4b0201003792bfdbf1a7781cbc9ee03539: {e}")

if __name__ == "__main__":
    main()
