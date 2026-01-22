import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('3f8c8c2377cb8e0daaf8073e8d03ac7d87580813')
        print(f"Checked out 3f8c8c2377cb8e0daaf8073e8d03ac7d87580813")
    except Exception as e:
        print(f"Failed to check out 3f8c8c2377cb8e0daaf8073e8d03ac7d87580813: {e}")

if __name__ == "__main__":
    main()
