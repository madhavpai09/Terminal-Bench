import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('cb383753c0e0eb52306e1024d32a782549c27e61')
        print(f"Checked out cb383753c0e0eb52306e1024d32a782549c27e61")
    except Exception as e:
        print(f"Failed to check out cb383753c0e0eb52306e1024d32a782549c27e61: {e}")

if __name__ == "__main__":
    main()
