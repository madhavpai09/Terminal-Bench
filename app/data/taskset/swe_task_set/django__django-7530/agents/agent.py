import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('f8fab6f90233c7114d642dfe01a4e6d4cb14ee7d')
        print(f"Checked out f8fab6f90233c7114d642dfe01a4e6d4cb14ee7d")
    except Exception as e:
        print(f"Failed to check out f8fab6f90233c7114d642dfe01a4e6d4cb14ee7d: {e}")

if __name__ == "__main__":
    main()
