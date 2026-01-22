import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/pydata/xarray"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('d3b6aa6d8b997df115a53c001d00222a0f92f63a')
        print(f"Checked out d3b6aa6d8b997df115a53c001d00222a0f92f63a")
    except Exception as e:
        print(f"Failed to check out d3b6aa6d8b997df115a53c001d00222a0f92f63a: {e}")

if __name__ == "__main__":
    main()
