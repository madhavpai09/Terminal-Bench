import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('2dfa7457f20ee187fbb09b5b6a1631da4458388c')
        print(f"Checked out 2dfa7457f20ee187fbb09b5b6a1631da4458388c")
    except Exception as e:
        print(f"Failed to check out 2dfa7457f20ee187fbb09b5b6a1631da4458388c: {e}")

if __name__ == "__main__":
    main()
