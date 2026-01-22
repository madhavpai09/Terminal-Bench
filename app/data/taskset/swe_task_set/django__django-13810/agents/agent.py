import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('429d089d0a8fbd400e0c010708df4f0d16218970')
        print(f"Checked out 429d089d0a8fbd400e0c010708df4f0d16218970")
    except Exception as e:
        print(f"Failed to check out 429d089d0a8fbd400e0c010708df4f0d16218970: {e}")

if __name__ == "__main__":
    main()
