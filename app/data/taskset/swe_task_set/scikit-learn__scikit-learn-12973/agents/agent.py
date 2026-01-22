import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/scikit-learn/scikit-learn"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('a7b8b9e9e16d4e15fabda5ae615086c2e1c47d8a')
        print(f"Checked out a7b8b9e9e16d4e15fabda5ae615086c2e1c47d8a")
    except Exception as e:
        print(f"Failed to check out a7b8b9e9e16d4e15fabda5ae615086c2e1c47d8a: {e}")

if __name__ == "__main__":
    main()
