import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/scikit-learn/scikit-learn"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('1c8668b0a021832386470ddf740d834e02c66f69')
        print(f"Checked out 1c8668b0a021832386470ddf740d834e02c66f69")
    except Exception as e:
        print(f"Failed to check out 1c8668b0a021832386470ddf740d834e02c66f69: {e}")

if __name__ == "__main__":
    main()
