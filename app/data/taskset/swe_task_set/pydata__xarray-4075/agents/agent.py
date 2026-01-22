import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/pydata/xarray"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('19b088636eb7d3f65ab7a1046ac672e0689371d8')
        print(f"Checked out 19b088636eb7d3f65ab7a1046ac672e0689371d8")
    except Exception as e:
        print(f"Failed to check out 19b088636eb7d3f65ab7a1046ac672e0689371d8: {e}")

if __name__ == "__main__":
    main()
