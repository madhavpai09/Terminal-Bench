import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('88664e6e0b781d0a8b5347896af74b555e92891e')
        print(f"Checked out 88664e6e0b781d0a8b5347896af74b555e92891e")
    except Exception as e:
        print(f"Failed to check out 88664e6e0b781d0a8b5347896af74b555e92891e: {e}")

if __name__ == "__main__":
    main()
