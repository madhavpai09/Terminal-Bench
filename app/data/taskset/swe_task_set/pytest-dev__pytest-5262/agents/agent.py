import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/pytest-dev/pytest"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('58e6a09db49f34886ff13f3b7520dd0bcd7063cd')
        print(f"Checked out 58e6a09db49f34886ff13f3b7520dd0bcd7063cd")
    except Exception as e:
        print(f"Failed to check out 58e6a09db49f34886ff13f3b7520dd0bcd7063cd: {e}")

if __name__ == "__main__":
    main()
