import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('7121bdf1facdd90d05b6994b4c2e5b2865a4638a')
        print(f"Checked out 7121bdf1facdd90d05b6994b4c2e5b2865a4638a")
    except Exception as e:
        print(f"Failed to check out 7121bdf1facdd90d05b6994b4c2e5b2865a4638a: {e}")

if __name__ == "__main__":
    main()
