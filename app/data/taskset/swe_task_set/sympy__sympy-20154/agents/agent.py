import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('bdb49c4abfb35554a3c8ce761696ffff3bb837fe')
        print(f"Checked out bdb49c4abfb35554a3c8ce761696ffff3bb837fe")
    except Exception as e:
        print(f"Failed to check out bdb49c4abfb35554a3c8ce761696ffff3bb837fe: {e}")

if __name__ == "__main__":
    main()
