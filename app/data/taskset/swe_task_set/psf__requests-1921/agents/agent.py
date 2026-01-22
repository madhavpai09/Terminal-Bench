import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/psf/requests"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('3c88e520da24ae6f736929a750876e7654accc3d')
        print(f"Checked out 3c88e520da24ae6f736929a750876e7654accc3d")
    except Exception as e:
        print(f"Failed to check out 3c88e520da24ae6f736929a750876e7654accc3d: {e}")

if __name__ == "__main__":
    main()
