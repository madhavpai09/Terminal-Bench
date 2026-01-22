import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('e245046bb6e8b32360aa48b8a41fb7050f0fc730')
        print(f"Checked out e245046bb6e8b32360aa48b8a41fb7050f0fc730")
    except Exception as e:
        print(f"Failed to check out e245046bb6e8b32360aa48b8a41fb7050f0fc730: {e}")

if __name__ == "__main__":
    main()
