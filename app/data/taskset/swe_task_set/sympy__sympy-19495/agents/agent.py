import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('25fbcce5b1a4c7e3956e6062930f4a44ce95a632')
        print(f"Checked out 25fbcce5b1a4c7e3956e6062930f4a44ce95a632")
    except Exception as e:
        print(f"Failed to check out 25fbcce5b1a4c7e3956e6062930f4a44ce95a632: {e}")

if __name__ == "__main__":
    main()
