import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/pytest-dev/pytest"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('cb828ebe70b4fa35cd5f9a7ee024272237eab351')
        print(f"Checked out cb828ebe70b4fa35cd5f9a7ee024272237eab351")
    except Exception as e:
        print(f"Failed to check out cb828ebe70b4fa35cd5f9a7ee024272237eab351: {e}")

if __name__ == "__main__":
    main()
