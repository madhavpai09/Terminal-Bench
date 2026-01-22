import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/astropy/astropy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('5250b2442501e6c671c6b380536f1edb352602d1')
        print(f"Checked out 5250b2442501e6c671c6b380536f1edb352602d1")
    except Exception as e:
        print(f"Failed to check out 5250b2442501e6c671c6b380536f1edb352602d1: {e}")

if __name__ == "__main__":
    main()
