import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('a708f39ce67af174df90c5b5e50ad1976cec7cb8')
        print(f"Checked out a708f39ce67af174df90c5b5e50ad1976cec7cb8")
    except Exception as e:
        print(f"Failed to check out a708f39ce67af174df90c5b5e50ad1976cec7cb8: {e}")

if __name__ == "__main__":
    main()
