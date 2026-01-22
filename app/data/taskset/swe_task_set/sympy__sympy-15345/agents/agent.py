import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('9ef28fba5b4d6d0168237c9c005a550e6dc27d81')
        print(f"Checked out 9ef28fba5b4d6d0168237c9c005a550e6dc27d81")
    except Exception as e:
        print(f"Failed to check out 9ef28fba5b4d6d0168237c9c005a550e6dc27d81: {e}")

if __name__ == "__main__":
    main()
