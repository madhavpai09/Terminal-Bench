import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('a7e7043c8746933dafce652507d3b821801cdc7d')
        print(f"Checked out a7e7043c8746933dafce652507d3b821801cdc7d")
    except Exception as e:
        print(f"Failed to check out a7e7043c8746933dafce652507d3b821801cdc7d: {e}")

if __name__ == "__main__":
    main()
