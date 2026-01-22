import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('e972620ada4f9ed7bc57f28e133e85c85b0a7b20')
        print(f"Checked out e972620ada4f9ed7bc57f28e133e85c85b0a7b20")
    except Exception as e:
        print(f"Failed to check out e972620ada4f9ed7bc57f28e133e85c85b0a7b20: {e}")

if __name__ == "__main__":
    main()
