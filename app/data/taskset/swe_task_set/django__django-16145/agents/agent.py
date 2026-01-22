import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('93d4c9ea1de24eb391cb2b3561b6703fd46374df')
        print(f"Checked out 93d4c9ea1de24eb391cb2b3561b6703fd46374df")
    except Exception as e:
        print(f"Failed to check out 93d4c9ea1de24eb391cb2b3561b6703fd46374df: {e}")

if __name__ == "__main__":
    main()
