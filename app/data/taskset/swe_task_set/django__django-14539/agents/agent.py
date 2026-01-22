import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('6a5ef557f80a8eb6a758ebe99c8bb477ca47459e')
        print(f"Checked out 6a5ef557f80a8eb6a758ebe99c8bb477ca47459e")
    except Exception as e:
        print(f"Failed to check out 6a5ef557f80a8eb6a758ebe99c8bb477ca47459e: {e}")

if __name__ == "__main__":
    main()
