import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('4e8121e8e42a24acc3565851c9ef50ca8322b15c')
        print(f"Checked out 4e8121e8e42a24acc3565851c9ef50ca8322b15c")
    except Exception as e:
        print(f"Failed to check out 4e8121e8e42a24acc3565851c9ef50ca8322b15c: {e}")

if __name__ == "__main__":
    main()
