import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('832c24fec1046eaa544a4cab4c69e3af3e651759')
        print(f"Checked out 832c24fec1046eaa544a4cab4c69e3af3e651759")
    except Exception as e:
        print(f"Failed to check out 832c24fec1046eaa544a4cab4c69e3af3e651759: {e}")

if __name__ == "__main__":
    main()
