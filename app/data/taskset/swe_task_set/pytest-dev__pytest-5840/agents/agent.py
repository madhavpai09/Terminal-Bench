import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/pytest-dev/pytest"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('73c5b7f4b11a81e971f7d1bb18072e06a87060f4')
        print(f"Checked out 73c5b7f4b11a81e971f7d1bb18072e06a87060f4")
    except Exception as e:
        print(f"Failed to check out 73c5b7f4b11a81e971f7d1bb18072e06a87060f4: {e}")

if __name__ == "__main__":
    main()
