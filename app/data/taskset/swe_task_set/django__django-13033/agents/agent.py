import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('a59de6e89e8dc1f3e71c9a5a5bbceb373ea5247e')
        print(f"Checked out a59de6e89e8dc1f3e71c9a5a5bbceb373ea5247e")
    except Exception as e:
        print(f"Failed to check out a59de6e89e8dc1f3e71c9a5a5bbceb373ea5247e: {e}")

if __name__ == "__main__":
    main()
