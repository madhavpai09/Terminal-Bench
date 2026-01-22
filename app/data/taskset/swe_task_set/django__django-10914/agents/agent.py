import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('e7fd69d051eaa67cb17f172a39b57253e9cb831a')
        print(f"Checked out e7fd69d051eaa67cb17f172a39b57253e9cb831a")
    except Exception as e:
        print(f"Failed to check out e7fd69d051eaa67cb17f172a39b57253e9cb831a: {e}")

if __name__ == "__main__":
    main()
