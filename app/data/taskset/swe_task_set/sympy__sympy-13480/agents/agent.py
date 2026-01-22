import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('f57fe3f4b3f2cab225749e1b3b38ae1bf80b62f0')
        print(f"Checked out f57fe3f4b3f2cab225749e1b3b38ae1bf80b62f0")
    except Exception as e:
        print(f"Failed to check out f57fe3f4b3f2cab225749e1b3b38ae1bf80b62f0: {e}")

if __name__ == "__main__":
    main()
