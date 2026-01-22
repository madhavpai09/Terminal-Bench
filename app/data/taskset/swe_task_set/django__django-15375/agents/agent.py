import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('beb7ddbcee03270e833b2f74927ccfc8027aa693')
        print(f"Checked out beb7ddbcee03270e833b2f74927ccfc8027aa693")
    except Exception as e:
        print(f"Failed to check out beb7ddbcee03270e833b2f74927ccfc8027aa693: {e}")

if __name__ == "__main__":
    main()
