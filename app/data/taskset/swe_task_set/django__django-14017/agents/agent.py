import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('466920f6d726eee90d5566e0a9948e92b33a122e')
        print(f"Checked out 466920f6d726eee90d5566e0a9948e92b33a122e")
    except Exception as e:
        print(f"Failed to check out 466920f6d726eee90d5566e0a9948e92b33a122e: {e}")

if __name__ == "__main__":
    main()
