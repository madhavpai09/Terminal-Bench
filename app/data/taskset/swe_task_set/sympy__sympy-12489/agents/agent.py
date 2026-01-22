import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('aa9780761ad8c3c0f68beeef3a0ce5caac9e100b')
        print(f"Checked out aa9780761ad8c3c0f68beeef3a0ce5caac9e100b")
    except Exception as e:
        print(f"Failed to check out aa9780761ad8c3c0f68beeef3a0ce5caac9e100b: {e}")

if __name__ == "__main__":
    main()
