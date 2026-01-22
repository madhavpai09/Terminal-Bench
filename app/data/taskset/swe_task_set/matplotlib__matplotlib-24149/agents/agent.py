import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/matplotlib/matplotlib"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('af39f1edffcd828f05cfdd04f2e59506bb4a27bc')
        print(f"Checked out af39f1edffcd828f05cfdd04f2e59506bb4a27bc")
    except Exception as e:
        print(f"Failed to check out af39f1edffcd828f05cfdd04f2e59506bb4a27bc: {e}")

if __name__ == "__main__":
    main()
