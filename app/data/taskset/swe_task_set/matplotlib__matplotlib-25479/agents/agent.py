import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/matplotlib/matplotlib"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('7fdf772201e4c9bafbc16dfac23b5472d6a53fa2')
        print(f"Checked out 7fdf772201e4c9bafbc16dfac23b5472d6a53fa2")
    except Exception as e:
        print(f"Failed to check out 7fdf772201e4c9bafbc16dfac23b5472d6a53fa2: {e}")

if __name__ == "__main__":
    main()
