import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/matplotlib/matplotlib"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('a3011dfd1aaa2487cce8aa7369475533133ef777')
        print(f"Checked out a3011dfd1aaa2487cce8aa7369475533133ef777")
    except Exception as e:
        print(f"Failed to check out a3011dfd1aaa2487cce8aa7369475533133ef777: {e}")

if __name__ == "__main__":
    main()
