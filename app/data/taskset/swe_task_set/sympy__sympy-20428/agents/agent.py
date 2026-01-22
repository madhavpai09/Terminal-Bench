import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('c0e85160406f9bf2bcaa2992138587668a1cd0bc')
        print(f"Checked out c0e85160406f9bf2bcaa2992138587668a1cd0bc")
    except Exception as e:
        print(f"Failed to check out c0e85160406f9bf2bcaa2992138587668a1cd0bc: {e}")

if __name__ == "__main__":
    main()
