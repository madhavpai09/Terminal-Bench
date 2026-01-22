import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/pytest-dev/pytest"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('e856638ba086fcf5bebf1bebea32d5cf78de87b4')
        print(f"Checked out e856638ba086fcf5bebf1bebea32d5cf78de87b4")
    except Exception as e:
        print(f"Failed to check out e856638ba086fcf5bebf1bebea32d5cf78de87b4: {e}")

if __name__ == "__main__":
    main()
