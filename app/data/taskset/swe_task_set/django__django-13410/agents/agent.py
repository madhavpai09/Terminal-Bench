import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('580a4341cb0b4cbfc215a70afc004875a7e815f4')
        print(f"Checked out 580a4341cb0b4cbfc215a70afc004875a7e815f4")
    except Exception as e:
        print(f"Failed to check out 580a4341cb0b4cbfc215a70afc004875a7e815f4: {e}")

if __name__ == "__main__":
    main()
