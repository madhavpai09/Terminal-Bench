import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('8dd5877f58f84f2b11126afbd0813e24545919ed')
        print(f"Checked out 8dd5877f58f84f2b11126afbd0813e24545919ed")
    except Exception as e:
        print(f"Failed to check out 8dd5877f58f84f2b11126afbd0813e24545919ed: {e}")

if __name__ == "__main__":
    main()
