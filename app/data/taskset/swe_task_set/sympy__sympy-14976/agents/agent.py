import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('9cbea134220b0b951587e11b63e2c832c7246cbc')
        print(f"Checked out 9cbea134220b0b951587e11b63e2c832c7246cbc")
    except Exception as e:
        print(f"Failed to check out 9cbea134220b0b951587e11b63e2c832c7246cbc: {e}")

if __name__ == "__main__":
    main()
