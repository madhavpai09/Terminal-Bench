import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('de32fe83a2e4a20887972c69a0693b94eb25a88b')
        print(f"Checked out de32fe83a2e4a20887972c69a0693b94eb25a88b")
    except Exception as e:
        print(f"Failed to check out de32fe83a2e4a20887972c69a0693b94eb25a88b: {e}")

if __name__ == "__main__":
    main()
