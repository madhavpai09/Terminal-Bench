import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('70381f282f2d9d039da860e391fe51649df2779d')
        print(f"Checked out 70381f282f2d9d039da860e391fe51649df2779d")
    except Exception as e:
        print(f"Failed to check out 70381f282f2d9d039da860e391fe51649df2779d: {e}")

if __name__ == "__main__":
    main()
