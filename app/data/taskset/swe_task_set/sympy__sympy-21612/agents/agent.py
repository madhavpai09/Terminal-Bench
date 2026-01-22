import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('b4777fdcef467b7132c055f8ac2c9a5059e6a145')
        print(f"Checked out b4777fdcef467b7132c055f8ac2c9a5059e6a145")
    except Exception as e:
        print(f"Failed to check out b4777fdcef467b7132c055f8ac2c9a5059e6a145: {e}")

if __name__ == "__main__":
    main()
