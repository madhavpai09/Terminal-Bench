import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('4a72da71001f154ea60906a2f74898d32b7322a7')
        print(f"Checked out 4a72da71001f154ea60906a2f74898d32b7322a7")
    except Exception as e:
        print(f"Failed to check out 4a72da71001f154ea60906a2f74898d32b7322a7: {e}")

if __name__ == "__main__":
    main()
