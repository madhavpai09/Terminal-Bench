import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('89d41cba392b759732ba9f1db4ff29ed47da6a56')
        print(f"Checked out 89d41cba392b759732ba9f1db4ff29ed47da6a56")
    except Exception as e:
        print(f"Failed to check out 89d41cba392b759732ba9f1db4ff29ed47da6a56: {e}")

if __name__ == "__main__":
    main()
