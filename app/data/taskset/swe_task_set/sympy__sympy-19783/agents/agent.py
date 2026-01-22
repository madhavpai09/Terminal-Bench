import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('586a43201d0357e92e8c93548d69a9f42bf548f4')
        print(f"Checked out 586a43201d0357e92e8c93548d69a9f42bf548f4")
    except Exception as e:
        print(f"Failed to check out 586a43201d0357e92e8c93548d69a9f42bf548f4: {e}")

if __name__ == "__main__":
    main()
