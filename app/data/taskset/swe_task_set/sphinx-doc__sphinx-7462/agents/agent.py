import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sphinx-doc/sphinx"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('b3e26a6c851133b82b50f4b68b53692076574d13')
        print(f"Checked out b3e26a6c851133b82b50f4b68b53692076574d13")
    except Exception as e:
        print(f"Failed to check out b3e26a6c851133b82b50f4b68b53692076574d13: {e}")

if __name__ == "__main__":
    main()
