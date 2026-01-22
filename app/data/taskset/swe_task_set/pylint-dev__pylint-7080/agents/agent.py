import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/pylint-dev/pylint"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('3c5eca2ded3dd2b59ebaf23eb289453b5d2930f0')
        print(f"Checked out 3c5eca2ded3dd2b59ebaf23eb289453b5d2930f0")
    except Exception as e:
        print(f"Failed to check out 3c5eca2ded3dd2b59ebaf23eb289453b5d2930f0: {e}")

if __name__ == "__main__":
    main()
