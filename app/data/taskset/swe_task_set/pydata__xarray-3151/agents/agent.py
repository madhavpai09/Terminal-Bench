import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/pydata/xarray"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('118f4d996e7711c9aced916e6049af9f28d5ec66')
        print(f"Checked out 118f4d996e7711c9aced916e6049af9f28d5ec66")
    except Exception as e:
        print(f"Failed to check out 118f4d996e7711c9aced916e6049af9f28d5ec66: {e}")

if __name__ == "__main__":
    main()
