import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/pylint-dev/pylint"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('273a8b25620467c1e5686aa8d2a1dbb8c02c78d0')
        print(f"Checked out 273a8b25620467c1e5686aa8d2a1dbb8c02c78d0")
    except Exception as e:
        print(f"Failed to check out 273a8b25620467c1e5686aa8d2a1dbb8c02c78d0: {e}")

if __name__ == "__main__":
    main()
