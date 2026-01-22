import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('0eb3e9bd754e4c9fac8b616b705178727fc8031e')
        print(f"Checked out 0eb3e9bd754e4c9fac8b616b705178727fc8031e")
    except Exception as e:
        print(f"Failed to check out 0eb3e9bd754e4c9fac8b616b705178727fc8031e: {e}")

if __name__ == "__main__":
    main()
