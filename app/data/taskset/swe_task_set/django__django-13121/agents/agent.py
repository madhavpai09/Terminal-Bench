import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('ec5aa2161d8015a3fe57dcbbfe14200cd18f0a16')
        print(f"Checked out ec5aa2161d8015a3fe57dcbbfe14200cd18f0a16")
    except Exception as e:
        print(f"Failed to check out ec5aa2161d8015a3fe57dcbbfe14200cd18f0a16: {e}")

if __name__ == "__main__":
    main()
