import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('de446c6d85f633271dfec1452f6f28ea783e293f')
        print(f"Checked out de446c6d85f633271dfec1452f6f28ea783e293f")
    except Exception as e:
        print(f"Failed to check out de446c6d85f633271dfec1452f6f28ea783e293f: {e}")

if __name__ == "__main__":
    main()
