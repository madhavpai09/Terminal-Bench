import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('e8fcdaad5c428878d0a5d6ba820d957013f75595')
        print(f"Checked out e8fcdaad5c428878d0a5d6ba820d957013f75595")
    except Exception as e:
        print(f"Failed to check out e8fcdaad5c428878d0a5d6ba820d957013f75595: {e}")

if __name__ == "__main__":
    main()
