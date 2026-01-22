import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('e065b293878b1e3ea56655aa9d33e87576cd77ff')
        print(f"Checked out e065b293878b1e3ea56655aa9d33e87576cd77ff")
    except Exception as e:
        print(f"Failed to check out e065b293878b1e3ea56655aa9d33e87576cd77ff: {e}")

if __name__ == "__main__":
    main()
