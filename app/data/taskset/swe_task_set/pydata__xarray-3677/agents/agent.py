import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/pydata/xarray"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('ef6e6a7b86f8479b9a1fecf15ad5b88a2326b31e')
        print(f"Checked out ef6e6a7b86f8479b9a1fecf15ad5b88a2326b31e")
    except Exception as e:
        print(f"Failed to check out ef6e6a7b86f8479b9a1fecf15ad5b88a2326b31e: {e}")

if __name__ == "__main__":
    main()
