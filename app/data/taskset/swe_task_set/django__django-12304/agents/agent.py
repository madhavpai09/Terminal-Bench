import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('4c1b401e8250f9f520b3c7dc369554477ce8b15a')
        print(f"Checked out 4c1b401e8250f9f520b3c7dc369554477ce8b15a")
    except Exception as e:
        print(f"Failed to check out 4c1b401e8250f9f520b3c7dc369554477ce8b15a: {e}")

if __name__ == "__main__":
    main()
