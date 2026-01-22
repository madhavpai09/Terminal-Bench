import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/pytest-dev/pytest"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('e6e300e729dd33956e5448d8be9a0b1540b4e53a')
        print(f"Checked out e6e300e729dd33956e5448d8be9a0b1540b4e53a")
    except Exception as e:
        print(f"Failed to check out e6e300e729dd33956e5448d8be9a0b1540b4e53a: {e}")

if __name__ == "__main__":
    main()
