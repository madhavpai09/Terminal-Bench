import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('838e432e3e5519c5383d12018e6c78f8ec7833c1')
        print(f"Checked out 838e432e3e5519c5383d12018e6c78f8ec7833c1")
    except Exception as e:
        print(f"Failed to check out 838e432e3e5519c5383d12018e6c78f8ec7833c1: {e}")

if __name__ == "__main__":
    main()
