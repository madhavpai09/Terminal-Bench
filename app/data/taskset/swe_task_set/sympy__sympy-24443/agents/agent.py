import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('809c53c077485ca48a206cee78340389cb83b7f1')
        print(f"Checked out 809c53c077485ca48a206cee78340389cb83b7f1")
    except Exception as e:
        print(f"Failed to check out 809c53c077485ca48a206cee78340389cb83b7f1: {e}")

if __name__ == "__main__":
    main()
