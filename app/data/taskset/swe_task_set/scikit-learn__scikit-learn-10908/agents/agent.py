import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/scikit-learn/scikit-learn"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('67d06b18c68ee4452768f8a1e868565dd4354abf')
        print(f"Checked out 67d06b18c68ee4452768f8a1e868565dd4354abf")
    except Exception as e:
        print(f"Failed to check out 67d06b18c68ee4452768f8a1e868565dd4354abf: {e}")

if __name__ == "__main__":
    main()
