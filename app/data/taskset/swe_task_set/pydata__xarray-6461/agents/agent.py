import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/pydata/xarray"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('851dadeb0338403e5021c3fbe80cbc9127ee672d')
        print(f"Checked out 851dadeb0338403e5021c3fbe80cbc9127ee672d")
    except Exception as e:
        print(f"Failed to check out 851dadeb0338403e5021c3fbe80cbc9127ee672d: {e}")

if __name__ == "__main__":
    main()
