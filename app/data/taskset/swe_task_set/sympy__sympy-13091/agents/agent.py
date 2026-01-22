import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('d1320814eda6549996190618a21eaf212cfd4d1e')
        print(f"Checked out d1320814eda6549996190618a21eaf212cfd4d1e")
    except Exception as e:
        print(f"Failed to check out d1320814eda6549996190618a21eaf212cfd4d1e: {e}")

if __name__ == "__main__":
    main()
