import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('bf47c719719d0e190a99fa2e7f959d5bbb7caf8a')
        print(f"Checked out bf47c719719d0e190a99fa2e7f959d5bbb7caf8a")
    except Exception as e:
        print(f"Failed to check out bf47c719719d0e190a99fa2e7f959d5bbb7caf8a: {e}")

if __name__ == "__main__":
    main()
