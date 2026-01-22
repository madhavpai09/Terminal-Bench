import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('910ecd1b8df7678f45c3d507dde6bcb1faafa243')
        print(f"Checked out 910ecd1b8df7678f45c3d507dde6bcb1faafa243")
    except Exception as e:
        print(f"Failed to check out 910ecd1b8df7678f45c3d507dde6bcb1faafa243: {e}")

if __name__ == "__main__":
    main()
