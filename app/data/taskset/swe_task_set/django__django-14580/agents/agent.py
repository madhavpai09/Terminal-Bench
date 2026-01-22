import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('36fa071d6ebd18a61c4d7f1b5c9d17106134bd44')
        print(f"Checked out 36fa071d6ebd18a61c4d7f1b5c9d17106134bd44")
    except Exception as e:
        print(f"Failed to check out 36fa071d6ebd18a61c4d7f1b5c9d17106134bd44: {e}")

if __name__ == "__main__":
    main()
