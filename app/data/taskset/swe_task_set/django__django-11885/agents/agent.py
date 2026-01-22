import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('04ac9b45a34440fa447feb6ae934687aacbfc5f4')
        print(f"Checked out 04ac9b45a34440fa447feb6ae934687aacbfc5f4")
    except Exception as e:
        print(f"Failed to check out 04ac9b45a34440fa447feb6ae934687aacbfc5f4: {e}")

if __name__ == "__main__":
    main()
