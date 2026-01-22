import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('9ffd4eae2ce7a7100c98f681e2b6ab818df384a4')
        print(f"Checked out 9ffd4eae2ce7a7100c98f681e2b6ab818df384a4")
    except Exception as e:
        print(f"Failed to check out 9ffd4eae2ce7a7100c98f681e2b6ab818df384a4: {e}")

if __name__ == "__main__":
    main()
