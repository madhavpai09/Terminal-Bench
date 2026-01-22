import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('71ae1ab0123582cc5bfe0f7d5f4cc19a9412f396')
        print(f"Checked out 71ae1ab0123582cc5bfe0f7d5f4cc19a9412f396")
    except Exception as e:
        print(f"Failed to check out 71ae1ab0123582cc5bfe0f7d5f4cc19a9412f396: {e}")

if __name__ == "__main__":
    main()
