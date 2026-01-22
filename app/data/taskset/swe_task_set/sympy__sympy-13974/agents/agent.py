import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('84c125972ad535b2dfb245f8d311d347b45e5b8a')
        print(f"Checked out 84c125972ad535b2dfb245f8d311d347b45e5b8a")
    except Exception as e:
        print(f"Failed to check out 84c125972ad535b2dfb245f8d311d347b45e5b8a: {e}")

if __name__ == "__main__":
    main()
