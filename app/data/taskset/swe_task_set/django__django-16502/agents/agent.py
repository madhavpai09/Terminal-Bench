import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('246eb4836a6fb967880f838aa0d22ecfdca8b6f1')
        print(f"Checked out 246eb4836a6fb967880f838aa0d22ecfdca8b6f1")
    except Exception as e:
        print(f"Failed to check out 246eb4836a6fb967880f838aa0d22ecfdca8b6f1: {e}")

if __name__ == "__main__":
    main()
