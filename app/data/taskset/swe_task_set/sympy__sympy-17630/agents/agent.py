import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('58e78209c8577b9890e957b624466e5beed7eb08')
        print(f"Checked out 58e78209c8577b9890e957b624466e5beed7eb08")
    except Exception as e:
        print(f"Failed to check out 58e78209c8577b9890e957b624466e5beed7eb08: {e}")

if __name__ == "__main__":
    main()
