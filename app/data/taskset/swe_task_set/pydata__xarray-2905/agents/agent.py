import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/pydata/xarray"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('7c4e2ac83f7b4306296ff9b7b51aaf016e5ad614')
        print(f"Checked out 7c4e2ac83f7b4306296ff9b7b51aaf016e5ad614")
    except Exception as e:
        print(f"Failed to check out 7c4e2ac83f7b4306296ff9b7b51aaf016e5ad614: {e}")

if __name__ == "__main__":
    main()
