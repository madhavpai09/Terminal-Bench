import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/pydata/xarray"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('37522e991a32ee3c0ad1a5ff8afe8e3eb1885550')
        print(f"Checked out 37522e991a32ee3c0ad1a5ff8afe8e3eb1885550")
    except Exception as e:
        print(f"Failed to check out 37522e991a32ee3c0ad1a5ff8afe8e3eb1885550: {e}")

if __name__ == "__main__":
    main()
