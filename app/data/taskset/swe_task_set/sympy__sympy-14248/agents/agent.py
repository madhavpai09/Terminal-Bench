import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('9986b38181cdd556a3f3411e553864f11912244e')
        print(f"Checked out 9986b38181cdd556a3f3411e553864f11912244e")
    except Exception as e:
        print(f"Failed to check out 9986b38181cdd556a3f3411e553864f11912244e: {e}")

if __name__ == "__main__":
    main()
