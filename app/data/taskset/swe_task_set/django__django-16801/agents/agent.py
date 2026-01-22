import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('3b62d8c83e3e48d2ed61cfa32a61c56d9e030293')
        print(f"Checked out 3b62d8c83e3e48d2ed61cfa32a61c56d9e030293")
    except Exception as e:
        print(f"Failed to check out 3b62d8c83e3e48d2ed61cfa32a61c56d9e030293: {e}")

if __name__ == "__main__":
    main()
