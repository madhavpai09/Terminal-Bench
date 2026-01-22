import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('fbacaa58ffc5a62456ee68b90efa13957f761ce4')
        print(f"Checked out fbacaa58ffc5a62456ee68b90efa13957f761ce4")
    except Exception as e:
        print(f"Failed to check out fbacaa58ffc5a62456ee68b90efa13957f761ce4: {e}")

if __name__ == "__main__":
    main()
