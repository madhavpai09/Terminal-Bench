import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('b8fe457a02cc24b3470ff678d0099c350b7fef43')
        print(f"Checked out b8fe457a02cc24b3470ff678d0099c350b7fef43")
    except Exception as e:
        print(f"Failed to check out b8fe457a02cc24b3470ff678d0099c350b7fef43: {e}")

if __name__ == "__main__":
    main()
