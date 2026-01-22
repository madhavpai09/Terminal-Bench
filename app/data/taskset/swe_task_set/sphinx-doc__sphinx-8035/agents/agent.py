import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sphinx-doc/sphinx"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('5e6da19f0e44a0ae83944fb6ce18f18f781e1a6e')
        print(f"Checked out 5e6da19f0e44a0ae83944fb6ce18f18f781e1a6e")
    except Exception as e:
        print(f"Failed to check out 5e6da19f0e44a0ae83944fb6ce18f18f781e1a6e: {e}")

if __name__ == "__main__":
    main()
