import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('09914ccf688974e068941f55412b930729bafa06')
        print(f"Checked out 09914ccf688974e068941f55412b930729bafa06")
    except Exception as e:
        print(f"Failed to check out 09914ccf688974e068941f55412b930729bafa06: {e}")

if __name__ == "__main__":
    main()
