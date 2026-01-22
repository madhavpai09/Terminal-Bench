import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('b1a4b1f0bdf05adbd3dc4dde14228e68da54c1a3')
        print(f"Checked out b1a4b1f0bdf05adbd3dc4dde14228e68da54c1a3")
    except Exception as e:
        print(f"Failed to check out b1a4b1f0bdf05adbd3dc4dde14228e68da54c1a3: {e}")

if __name__ == "__main__":
    main()
