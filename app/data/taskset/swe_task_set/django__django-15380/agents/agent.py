import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('71e7c8e73712419626f1c2b6ec036e8559a2d667')
        print(f"Checked out 71e7c8e73712419626f1c2b6ec036e8559a2d667")
    except Exception as e:
        print(f"Failed to check out 71e7c8e73712419626f1c2b6ec036e8559a2d667: {e}")

if __name__ == "__main__":
    main()
