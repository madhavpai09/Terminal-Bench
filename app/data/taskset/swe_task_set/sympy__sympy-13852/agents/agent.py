import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('c935e1d106743efd5bf0705fbeedbd18fadff4dc')
        print(f"Checked out c935e1d106743efd5bf0705fbeedbd18fadff4dc")
    except Exception as e:
        print(f"Failed to check out c935e1d106743efd5bf0705fbeedbd18fadff4dc: {e}")

if __name__ == "__main__":
    main()
