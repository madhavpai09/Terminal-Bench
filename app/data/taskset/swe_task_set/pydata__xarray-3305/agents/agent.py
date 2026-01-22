import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/pydata/xarray"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('69c7e01e5167a3137c285cb50d1978252bb8bcbf')
        print(f"Checked out 69c7e01e5167a3137c285cb50d1978252bb8bcbf")
    except Exception as e:
        print(f"Failed to check out 69c7e01e5167a3137c285cb50d1978252bb8bcbf: {e}")

if __name__ == "__main__":
    main()
