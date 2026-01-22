import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('1f8382d34d54061eddc41df6994e20ee38c60907')
        print(f"Checked out 1f8382d34d54061eddc41df6994e20ee38c60907")
    except Exception as e:
        print(f"Failed to check out 1f8382d34d54061eddc41df6994e20ee38c60907: {e}")

if __name__ == "__main__":
    main()
