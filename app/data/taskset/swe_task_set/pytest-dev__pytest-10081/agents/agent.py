import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/pytest-dev/pytest"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('da9a2b584eb7a6c7e924b2621ed0ddaeca0a7bea')
        print(f"Checked out da9a2b584eb7a6c7e924b2621ed0ddaeca0a7bea")
    except Exception as e:
        print(f"Failed to check out da9a2b584eb7a6c7e924b2621ed0ddaeca0a7bea: {e}")

if __name__ == "__main__":
    main()
