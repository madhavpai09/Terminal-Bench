import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/pylint-dev/pylint"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('754b487f4d892e3d4872b6fc7468a71db4e31c13')
        print(f"Checked out 754b487f4d892e3d4872b6fc7468a71db4e31c13")
    except Exception as e:
        print(f"Failed to check out 754b487f4d892e3d4872b6fc7468a71db4e31c13: {e}")

if __name__ == "__main__":
    main()
