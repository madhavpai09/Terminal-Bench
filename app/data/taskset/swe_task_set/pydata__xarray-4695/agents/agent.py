import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/pydata/xarray"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('51ef2a66c4e0896eab7d2b03e3dfb3963e338e3c')
        print(f"Checked out 51ef2a66c4e0896eab7d2b03e3dfb3963e338e3c")
    except Exception as e:
        print(f"Failed to check out 51ef2a66c4e0896eab7d2b03e3dfb3963e338e3c: {e}")

if __name__ == "__main__":
    main()
