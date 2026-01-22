import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/sphinx-doc/sphinx"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('57ed10c68057c96491acbd3e62254ccfaf9e3861')
        print(f"Checked out 57ed10c68057c96491acbd3e62254ccfaf9e3861")
    except Exception as e:
        print(f"Failed to check out 57ed10c68057c96491acbd3e62254ccfaf9e3861: {e}")

if __name__ == "__main__":
    main()
