import git
import os

def main():
    repo_path = "/Users/jmadhavpai/Desktop/Terminal-bench/environment/src/django/django"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('5573a54d409bb98b5c5acdb308310bed02d392c2')
        print(f"Checked out 5573a54d409bb98b5c5acdb308310bed02d392c2")
    except Exception as e:
        print(f"Failed to check out 5573a54d409bb98b5c5acdb308310bed02d392c2: {e}")

if __name__ == "__main__":
    main()
