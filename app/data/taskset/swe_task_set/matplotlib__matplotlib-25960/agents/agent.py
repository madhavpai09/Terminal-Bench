import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/matplotlib/matplotlib"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('1d0d255b79e84dfc9f2123c5eb85a842d342f72b')
        print(f"Checked out 1d0d255b79e84dfc9f2123c5eb85a842d342f72b")
    except Exception as e:
        print(f"Failed to check out 1d0d255b79e84dfc9f2123c5eb85a842d342f72b: {e}")

if __name__ == "__main__":
    main()
