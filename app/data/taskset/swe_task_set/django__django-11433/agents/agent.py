import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('21b1d239125f1228e579b1ce8d94d4d5feadd2a6')
        print(f"Checked out 21b1d239125f1228e579b1ce8d94d4d5feadd2a6")
    except Exception as e:
        print(f"Failed to check out 21b1d239125f1228e579b1ce8d94d4d5feadd2a6: {e}")

if __name__ == "__main__":
    main()
