import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('d4df5e1b0b1c643fe0fc521add0236764ec8e92a')
        print(f"Checked out d4df5e1b0b1c643fe0fc521add0236764ec8e92a")
    except Exception as e:
        print(f"Failed to check out d4df5e1b0b1c643fe0fc521add0236764ec8e92a: {e}")

if __name__ == "__main__":
    main()
