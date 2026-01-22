import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('51c9bb7cd16081133af4f0ab6d06572660309730')
        print(f"Checked out 51c9bb7cd16081133af4f0ab6d06572660309730")
    except Exception as e:
        print(f"Failed to check out 51c9bb7cd16081133af4f0ab6d06572660309730: {e}")

if __name__ == "__main__":
    main()
