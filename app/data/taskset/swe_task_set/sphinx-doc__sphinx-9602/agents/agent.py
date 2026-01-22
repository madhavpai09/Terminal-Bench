import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sphinx-doc/sphinx"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('6c38f68dae221e8cfc70c137974b8b88bd3baaab')
        print(f"Checked out 6c38f68dae221e8cfc70c137974b8b88bd3baaab")
    except Exception as e:
        print(f"Failed to check out 6c38f68dae221e8cfc70c137974b8b88bd3baaab: {e}")

if __name__ == "__main__":
    main()
