import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/pydata/xarray"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('a41edc7bf5302f2ea327943c0c48c532b12009bc')
        print(f"Checked out a41edc7bf5302f2ea327943c0c48c532b12009bc")
    except Exception as e:
        print(f"Failed to check out a41edc7bf5302f2ea327943c0c48c532b12009bc: {e}")

if __name__ == "__main__":
    main()
