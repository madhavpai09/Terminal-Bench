import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('6810dee426943c1a2fe85b5002dd0d4cf2246a05')
        print(f"Checked out 6810dee426943c1a2fe85b5002dd0d4cf2246a05")
    except Exception as e:
        print(f"Failed to check out 6810dee426943c1a2fe85b5002dd0d4cf2246a05: {e}")

if __name__ == "__main__":
    main()
