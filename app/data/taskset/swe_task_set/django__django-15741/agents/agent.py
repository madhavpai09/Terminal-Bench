import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('8c0886b068ba4e224dd78104b93c9638b860b398')
        print(f"Checked out 8c0886b068ba4e224dd78104b93c9638b860b398")
    except Exception as e:
        print(f"Failed to check out 8c0886b068ba4e224dd78104b93c9638b860b398: {e}")

if __name__ == "__main__":
    main()
