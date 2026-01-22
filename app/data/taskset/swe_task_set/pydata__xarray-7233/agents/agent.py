import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/pydata/xarray"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('51d37d1be95547059251076b3fadaa317750aab3')
        print(f"Checked out 51d37d1be95547059251076b3fadaa317750aab3")
    except Exception as e:
        print(f"Failed to check out 51d37d1be95547059251076b3fadaa317750aab3: {e}")

if __name__ == "__main__":
    main()
