import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('d90e34c61b27fba2527834806639eebbcfab9631')
        print(f"Checked out d90e34c61b27fba2527834806639eebbcfab9631")
    except Exception as e:
        print(f"Failed to check out d90e34c61b27fba2527834806639eebbcfab9631: {e}")

if __name__ == "__main__":
    main()
