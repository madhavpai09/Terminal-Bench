import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sphinx-doc/sphinx"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('9ed054279aeffd5b1d0642e2d24a8800389de29f')
        print(f"Checked out 9ed054279aeffd5b1d0642e2d24a8800389de29f")
    except Exception as e:
        print(f"Failed to check out 9ed054279aeffd5b1d0642e2d24a8800389de29f: {e}")

if __name__ == "__main__":
    main()
