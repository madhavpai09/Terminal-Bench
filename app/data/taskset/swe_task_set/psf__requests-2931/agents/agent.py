import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/psf/requests"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('5f7a3a74aab1625c2bb65f643197ee885e3da576')
        print(f"Checked out 5f7a3a74aab1625c2bb65f643197ee885e3da576")
    except Exception as e:
        print(f"Failed to check out 5f7a3a74aab1625c2bb65f643197ee885e3da576: {e}")

if __name__ == "__main__":
    main()
