import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('28d5262fa3315690395f04e3619ed554dbaf725b')
        print(f"Checked out 28d5262fa3315690395f04e3619ed554dbaf725b")
    except Exception as e:
        print(f"Failed to check out 28d5262fa3315690395f04e3619ed554dbaf725b: {e}")

if __name__ == "__main__":
    main()
