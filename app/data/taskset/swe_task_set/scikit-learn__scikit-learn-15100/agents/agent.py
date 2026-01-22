import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/scikit-learn/scikit-learn"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('af8a6e592a1a15d92d77011856d5aa0ec4db4c6c')
        print(f"Checked out af8a6e592a1a15d92d77011856d5aa0ec4db4c6c")
    except Exception as e:
        print(f"Failed to check out af8a6e592a1a15d92d77011856d5aa0ec4db4c6c: {e}")

if __name__ == "__main__":
    main()
