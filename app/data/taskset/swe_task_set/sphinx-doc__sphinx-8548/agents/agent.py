import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sphinx-doc/sphinx"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('dd1615c59dc6fff633e27dbb3861f2d27e1fb976')
        print(f"Checked out dd1615c59dc6fff633e27dbb3861f2d27e1fb976")
    except Exception as e:
        print(f"Failed to check out dd1615c59dc6fff633e27dbb3861f2d27e1fb976: {e}")

if __name__ == "__main__":
    main()
