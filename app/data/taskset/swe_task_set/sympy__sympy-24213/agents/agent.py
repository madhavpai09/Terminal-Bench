import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('e8c22f6eac7314be8d92590bfff92ced79ee03e2')
        print(f"Checked out e8c22f6eac7314be8d92590bfff92ced79ee03e2")
    except Exception as e:
        print(f"Failed to check out e8c22f6eac7314be8d92590bfff92ced79ee03e2: {e}")

if __name__ == "__main__":
    main()
