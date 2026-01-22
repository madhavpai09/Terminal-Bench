import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sphinx-doc/sphinx"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('795747bdb6b8fb7d717d5bbfc2c3316869e66a73')
        print(f"Checked out 795747bdb6b8fb7d717d5bbfc2c3316869e66a73")
    except Exception as e:
        print(f"Failed to check out 795747bdb6b8fb7d717d5bbfc2c3316869e66a73: {e}")

if __name__ == "__main__":
    main()
