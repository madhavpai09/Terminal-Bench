import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('6efc35b4fe3009666e56a60af0675d7d532bf4ff')
        print(f"Checked out 6efc35b4fe3009666e56a60af0675d7d532bf4ff")
    except Exception as e:
        print(f"Failed to check out 6efc35b4fe3009666e56a60af0675d7d532bf4ff: {e}")

if __name__ == "__main__":
    main()
