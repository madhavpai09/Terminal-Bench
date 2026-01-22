import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('ece18207cbb64dd89014e279ac636a6c9829828e')
        print(f"Checked out ece18207cbb64dd89014e279ac636a6c9829828e")
    except Exception as e:
        print(f"Failed to check out ece18207cbb64dd89014e279ac636a6c9829828e: {e}")

if __name__ == "__main__":
    main()
