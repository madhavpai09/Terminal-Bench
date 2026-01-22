import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('360290c4c401e386db60723ddb0109ed499c9f6e')
        print(f"Checked out 360290c4c401e386db60723ddb0109ed499c9f6e")
    except Exception as e:
        print(f"Failed to check out 360290c4c401e386db60723ddb0109ed499c9f6e: {e}")

if __name__ == "__main__":
    main()
