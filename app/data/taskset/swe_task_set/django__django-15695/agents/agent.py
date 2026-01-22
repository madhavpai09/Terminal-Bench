import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('647480166bfe7532e8c471fef0146e3a17e6c0c9')
        print(f"Checked out 647480166bfe7532e8c471fef0146e3a17e6c0c9")
    except Exception as e:
        print(f"Failed to check out 647480166bfe7532e8c471fef0146e3a17e6c0c9: {e}")

if __name__ == "__main__":
    main()
