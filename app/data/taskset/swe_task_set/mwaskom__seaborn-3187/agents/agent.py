import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/mwaskom/seaborn"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('22cdfb0c93f8ec78492d87edb810f10cb7f57a31')
        print(f"Checked out 22cdfb0c93f8ec78492d87edb810f10cb7f57a31")
    except Exception as e:
        print(f"Failed to check out 22cdfb0c93f8ec78492d87edb810f10cb7f57a31: {e}")

if __name__ == "__main__":
    main()
