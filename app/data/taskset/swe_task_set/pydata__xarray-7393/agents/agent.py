import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/pydata/xarray"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('41fef6f1352be994cd90056d47440fe9aa4c068f')
        print(f"Checked out 41fef6f1352be994cd90056d47440fe9aa4c068f")
    except Exception as e:
        print(f"Failed to check out 41fef6f1352be994cd90056d47440fe9aa4c068f: {e}")

if __name__ == "__main__":
    main()
