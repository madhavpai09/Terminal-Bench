import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('973fa566521037ac140dcece73fceae50ee522f1')
        print(f"Checked out 973fa566521037ac140dcece73fceae50ee522f1")
    except Exception as e:
        print(f"Failed to check out 973fa566521037ac140dcece73fceae50ee522f1: {e}")

if __name__ == "__main__":
    main()
