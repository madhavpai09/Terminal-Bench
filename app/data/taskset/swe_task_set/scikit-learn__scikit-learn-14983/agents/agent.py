import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/scikit-learn/scikit-learn"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('06632c0d185128a53c57ccc73b25b6408e90bb89')
        print(f"Checked out 06632c0d185128a53c57ccc73b25b6408e90bb89")
    except Exception as e:
        print(f"Failed to check out 06632c0d185128a53c57ccc73b25b6408e90bb89: {e}")

if __name__ == "__main__":
    main()
