import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('bef6f7584280f1cc80e5e2d80b7ad073a93d26ec')
        print(f"Checked out bef6f7584280f1cc80e5e2d80b7ad073a93d26ec")
    except Exception as e:
        print(f"Failed to check out bef6f7584280f1cc80e5e2d80b7ad073a93d26ec: {e}")

if __name__ == "__main__":
    main()
