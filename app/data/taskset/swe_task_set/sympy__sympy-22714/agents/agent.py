import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('3ff4717b6aef6086e78f01cdfa06f64ae23aed7e')
        print(f"Checked out 3ff4717b6aef6086e78f01cdfa06f64ae23aed7e")
    except Exception as e:
        print(f"Failed to check out 3ff4717b6aef6086e78f01cdfa06f64ae23aed7e: {e}")

if __name__ == "__main__":
    main()
