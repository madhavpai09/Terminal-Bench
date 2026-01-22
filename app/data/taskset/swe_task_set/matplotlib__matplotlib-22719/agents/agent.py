import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/matplotlib/matplotlib"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('a2a1b0a11b993fe5f8fab64b6161e99243a6393c')
        print(f"Checked out a2a1b0a11b993fe5f8fab64b6161e99243a6393c")
    except Exception as e:
        print(f"Failed to check out a2a1b0a11b993fe5f8fab64b6161e99243a6393c: {e}")

if __name__ == "__main__":
    main()
