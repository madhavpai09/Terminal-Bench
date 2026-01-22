import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('c6350d594c359151ee17b0c4f354bb44f28ff69e')
        print(f"Checked out c6350d594c359151ee17b0c4f354bb44f28ff69e")
    except Exception as e:
        print(f"Failed to check out c6350d594c359151ee17b0c4f354bb44f28ff69e: {e}")

if __name__ == "__main__":
    main()
