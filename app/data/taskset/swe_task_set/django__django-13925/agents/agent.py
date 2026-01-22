import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('0c42cdf0d2422f4c080e93594d5d15381d6e955e')
        print(f"Checked out 0c42cdf0d2422f4c080e93594d5d15381d6e955e")
    except Exception as e:
        print(f"Failed to check out 0c42cdf0d2422f4c080e93594d5d15381d6e955e: {e}")

if __name__ == "__main__":
    main()
