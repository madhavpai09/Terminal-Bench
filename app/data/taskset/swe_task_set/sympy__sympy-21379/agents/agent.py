import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sympy/sympy"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('624217179aaf8d094e6ff75b7493ad1ee47599b0')
        print(f"Checked out 624217179aaf8d094e6ff75b7493ad1ee47599b0")
    except Exception as e:
        print(f"Failed to check out 624217179aaf8d094e6ff75b7493ad1ee47599b0: {e}")

if __name__ == "__main__":
    main()
