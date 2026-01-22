import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/pytest-dev/pytest"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('19ad5889353c7f5f2b65cc2acd346b7a9e95dfcd')
        print(f"Checked out 19ad5889353c7f5f2b65cc2acd346b7a9e95dfcd")
    except Exception as e:
        print(f"Failed to check out 19ad5889353c7f5f2b65cc2acd346b7a9e95dfcd: {e}")

if __name__ == "__main__":
    main()
