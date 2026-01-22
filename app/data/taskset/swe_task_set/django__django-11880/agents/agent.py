import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('06909fe084f87a65459a83bd69d7cdbe4fce9a7c')
        print(f"Checked out 06909fe084f87a65459a83bd69d7cdbe4fce9a7c")
    except Exception as e:
        print(f"Failed to check out 06909fe084f87a65459a83bd69d7cdbe4fce9a7c: {e}")

if __name__ == "__main__":
    main()
