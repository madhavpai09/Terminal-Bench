import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/pydata/xarray"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('45c0a114e2b7b27b83c9618bc05b36afac82183c')
        print(f"Checked out 45c0a114e2b7b27b83c9618bc05b36afac82183c")
    except Exception as e:
        print(f"Failed to check out 45c0a114e2b7b27b83c9618bc05b36afac82183c: {e}")

if __name__ == "__main__":
    main()
