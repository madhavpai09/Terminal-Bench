import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('8c3bd0b708b488a1f6e8bd8cc6b96569904605be')
        print(f"Checked out 8c3bd0b708b488a1f6e8bd8cc6b96569904605be")
    except Exception as e:
        print(f"Failed to check out 8c3bd0b708b488a1f6e8bd8cc6b96569904605be: {e}")

if __name__ == "__main__":
    main()
