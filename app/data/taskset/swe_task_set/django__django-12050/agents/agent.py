import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('b93a0e34d9b9b99d41103782b7e7aeabf47517e3')
        print(f"Checked out b93a0e34d9b9b99d41103782b7e7aeabf47517e3")
    except Exception as e:
        print(f"Failed to check out b93a0e34d9b9b99d41103782b7e7aeabf47517e3: {e}")

if __name__ == "__main__":
    main()
