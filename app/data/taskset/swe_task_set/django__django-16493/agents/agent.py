import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('e3a4cee081cf60650b8824f0646383b79cb110e7')
        print(f"Checked out e3a4cee081cf60650b8824f0646383b79cb110e7")
    except Exception as e:
        print(f"Failed to check out e3a4cee081cf60650b8824f0646383b79cb110e7: {e}")

if __name__ == "__main__":
    main()
