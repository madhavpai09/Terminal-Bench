import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('0af9a5fc7d765aa05ea784e2c3237675f3bb4b49')
        print(f"Checked out 0af9a5fc7d765aa05ea784e2c3237675f3bb4b49")
    except Exception as e:
        print(f"Failed to check out 0af9a5fc7d765aa05ea784e2c3237675f3bb4b49: {e}")

if __name__ == "__main__":
    main()
