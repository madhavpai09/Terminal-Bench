import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('447980e72ac01da1594dd3373a03ba40b7ee6f80')
        print(f"Checked out 447980e72ac01da1594dd3373a03ba40b7ee6f80")
    except Exception as e:
        print(f"Failed to check out 447980e72ac01da1594dd3373a03ba40b7ee6f80: {e}")

if __name__ == "__main__":
    main()
