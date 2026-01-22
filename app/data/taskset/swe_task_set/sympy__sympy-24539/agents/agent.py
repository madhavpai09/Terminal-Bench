import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('193e3825645d93c73e31cdceb6d742cc6919624d')
        print(f"Checked out 193e3825645d93c73e31cdceb6d742cc6919624d")
    except Exception as e:
        print(f"Failed to check out 193e3825645d93c73e31cdceb6d742cc6919624d: {e}")

if __name__ == "__main__":
    main()
