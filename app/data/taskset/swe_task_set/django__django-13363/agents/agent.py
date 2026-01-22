import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('76e0151ea0e0f56dca66cee846a78b89346d2c4c')
        print(f"Checked out 76e0151ea0e0f56dca66cee846a78b89346d2c4c")
    except Exception as e:
        print(f"Failed to check out 76e0151ea0e0f56dca66cee846a78b89346d2c4c: {e}")

if __name__ == "__main__":
    main()
