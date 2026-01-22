import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('a3475b3f9ac662cd425157dd3bdb93ad7111c090')
        print(f"Checked out a3475b3f9ac662cd425157dd3bdb93ad7111c090")
    except Exception as e:
        print(f"Failed to check out a3475b3f9ac662cd425157dd3bdb93ad7111c090: {e}")

if __name__ == "__main__":
    main()
