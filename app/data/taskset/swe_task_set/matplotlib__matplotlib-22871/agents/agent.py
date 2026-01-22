import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/matplotlib/matplotlib"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('a7b7260bf06c20d408215d95ce20a1a01c12e5b1')
        print(f"Checked out a7b7260bf06c20d408215d95ce20a1a01c12e5b1")
    except Exception as e:
        print(f"Failed to check out a7b7260bf06c20d408215d95ce20a1a01c12e5b1: {e}")

if __name__ == "__main__":
    main()
