import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('6f54459aa0248bf1467ad12ee6333d8bc924a642')
        print(f"Checked out 6f54459aa0248bf1467ad12ee6333d8bc924a642")
    except Exception as e:
        print(f"Failed to check out 6f54459aa0248bf1467ad12ee6333d8bc924a642: {e}")

if __name__ == "__main__":
    main()
